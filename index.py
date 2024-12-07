from flask import Flask, render_template
from faker import Faker

fake=Faker()
list=("name","address","calendar","text","credit_card","email","phone_number","colors","company")
app = Flask(__name__)
length=len(list)

@app.route("/")
def index():
    return render_template("front.html", lista=list, length=length)

@app.route("/allow/<selection>")
def selection(selection):
    if not list.__contains__(selection):
        return "Wrong selection"
    else:
        return render_template(selection+".html", selection=selection)        

@app.route("/allow/<results>/<int:digit>")
def results(results, digit):
    instances=[getattr(fake,results)() for i in range(digit)]
    print(instances)
    return render_template("results.html", results=instances, digit=digit) 


if __name__ == '__main__':
    app.run(host='localhost', port=8000)