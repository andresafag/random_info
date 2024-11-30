from flask import Flask, render_template
from faker import Faker

fake=Faker()
list=("name","address","date","country","text","location","credit card","email","phone number","color","company")
app = Flask(__name__)
length=len(list)

@app.route("/")
def index():
    return render_template("front.html", lista=list, length=length)


if __name__ == '__main__':
    app.run(host='localhost', port=8000)