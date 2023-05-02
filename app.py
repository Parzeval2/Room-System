from flask import Flask, render_template
from . import db
from . import queueobject

app = Flask(__name__)

@app.route('/')
def index():

    data = ("Queue Order:       Group's CWID:")

    for i in range(len(queueobject.groups)):
        id = queueobject.groups[i]
        group = GroupInfo.query.filter(GroupInfo.id == id).first()
        
        code = group.CWID
        info = (f"   {i+1}               {code}")

        data.append(info)


    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)