from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("front.html", title="titulo", description="descripcion")


if __name__ == '__main__':
    app.run(host='localhost', port=8000)

