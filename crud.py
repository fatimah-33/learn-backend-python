from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy 

app= Flask(__name__)
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html',data[{
        'items:1' },{
        'items:2'},{
        'items:3'}])
