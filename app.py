from flask import Flask, render_template
#setup for flask app
app = Flask(__name__)

############################
#Debug
app.debug = False
############################


@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")
