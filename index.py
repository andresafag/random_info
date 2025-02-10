from flask import Flask, render_template
from faker import Faker
import datetime
import csv
from helpers import name
import json
import urllib.parse


fake=Faker()
list=("name","address","date","text","credit_card","email","phone_number","colors","company")
list_items_description=("When running out of creativity when it comes to come up with names this is the best option","Address can be complicated so this is the right tool for you","Date","There exist thousands of words in the world so what better way than clicking on this","Credit card information is a repetitive task that can end up being cumbersome before this came along","Randomized email@whatever will be found here","Phone Numbers kdjsaljdjsdjsjldjasjdajdsklasjdjlsjldjlasjkdj","Colors jdsljdljskjdjiejoewruioewuiorueoiuewriouewcnmnc","Company asdsñdlslñsdñaovmcnm,nwenwq,n")
app = Flask(__name__)
length=len(list)


@app.route("/")
def index():
    return render_template("front.html", lista=list,list_items_description=list_items_description)


@app.route("/allow/<selection>")
def selection(selection):
    if not list.__contains__(selection):
        return "Wrong selection"
    else:
        return render_template(selection+".html", selection=selection)        

@app.route("/allow/<results>/<int:digit>")
def results(results, digit):
    instancess=[]
    instances=[getattr(fake,results)() for i in range(digit)]
       
    for i in instances:
        instancess.append([i])
    
    return render_template("results.html", results=instancess, digit=digit) 

@app.route("/allow/<results>/<int:digit>/<start>/<end>/")
def resultsbetween(results, digit,start,end):
    instancess=[]
    startDate = datetime.datetime.strptime(start, "%Y-%m-%d").date()
    endDate = datetime.datetime.strptime(end, "%Y-%m-%d").date()
    
    res=[fake.date_between(start_date=startDate, end_date=endDate) for i in range(digit)]    
    
    for item in range(digit):
        instancess.append([res[item].strftime("%Y-%m-%d")])
    
    return render_template("results.html", results=instancess, digit=digit) 

@app.route("/download/<params>/")
def download(params):
    decoded_params = urllib.parse.unquote(params)
    try:
        allData = json.loads(decoded_params)
        # Specify the file name
        filename = "output.csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for row in allData:
                writer.writerow([row])
    except json.JSONDecodeError:
        return "Invalid JSON format"    
    return "Downloaded"


if __name__ == '__main__':
    app.run(host='localhost', port=8000)