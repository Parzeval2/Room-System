from flask import Flask, render_template
import Group_Class
import Queue
#setup for flask app
app = Flask(__name__)

############################
#Debug
app.debug = False
############################
queue = Queue.Queue()

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")

@app.route('/register_group')

@app.route('/join_queue')
def join_queue(group):
    queue.join_queue(group)
    return render_template('queue.html', queue=queue)