from flask import Flask, render_template, Response, request
from faker import Faker
import datetime
import csv
import io
import json
import urllib.parse
import serverless_wsgi


allowed_results=("name","address","date","text","credit_card","email","phone_number","colors","company")
list_items_description=("When running out of creativity when it comes to come up with names this is the best option","Address can be complicated so this is the right tool for you","Date","There exist thousands of words in the world so what better way than clicking on this","Credit card information is a repetitive task that can end up being cumbersome before this came along","Randomized email@whatever will be found here","Phone Numbers of any kind","Colors in various formats","Company of every kind")
application = Flask(__name__)
length=len(allowed_results)


@application.route("/")
def index():
    return render_template("front.html", lista=allowed_results, list_items_description=list_items_description)


@application.route("/allow/<selection>")
def selection(selection):
    if selection not in allowed_results:
        return "Wrong selection"
    else:
        return render_template(selection+".html", selection=selection)        

@application.route("/allow/<results>/<int:digit>/<locale>")
def results(results, digit, locale):
    fake=Faker(locale)
    instancess=[]
    instances=[getattr(fake,results)() for i in range(digit)]
       
    for i in instances:
        instancess.append(i)
    
    return render_template("results.html", results=instancess, digit=digit) 

@application.route("/allow/<results>/<int:digit>/<start>/<end>/")
def resultsbetween(results, digit,start,end):
    fake=Faker()
    instancess=[]
    startDate = datetime.datetime.strptime(start, "%Y-%m-%d").date()
    endDate = datetime.datetime.strptime(end, "%Y-%m-%d").date()
    
    res=[fake.date_between(start_date=startDate, end_date=endDate) for i in range(digit)]    
    
    for item in range(digit):
        instancess.append(res[item].strftime("%Y-%m-%d"))
    
    return render_template("results.html", results=instancess, digit=digit) 

@application.route("/download/", methods=["POST"])
def download():
    try:
        allData = request.get_json()
        output = io.StringIO()
        writer = csv.writer(output)
        for row in allData:
            writer.writerow([row])
        return Response(
            output.getvalue(),
            mimetype="text/csv",
            headers={"Content-Disposition": "attachment; filename=output.csv"}
        )
    except Exception:
        return "Invalid data", 400

def handler(event, context):
    return serverless_wsgi.handle_request(application, event, context)

if __name__ == '__main__':
    application.run(host="0.0.0.0", port=5000)