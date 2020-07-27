# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request,redirect
from flask_pymongo import PyMongo


# -- Initialization section --
app = Flask(__name__)

events = [
        {"event":"First Day of Classes", "date":"2019-08-21"},
        {"event":"Winter Break", "date":"2019-12-20"},
        {"event":"Finals Begin", "date":"2019-12-01"},
        {"event":"Dwaynes Bday", "date":""},

    ]

# name of database
app.config['MONGO_DBNAME'] = 'Test'

# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://Admin:HEGLYNBVdjtOHW8y@cluster0.quoam.mongodb.net/Test?retryWrites=true&w=majority'

mongo = PyMongo(app)

# -- Routes section --
# INDEX

@app.route('/')
@app.route('/index')

def index():
    collection=mongo.db.events
    #events = collection.find({}) #gives all infor if database
    #events = collection.find({"event":"Upper"}) #gives all items that match the query
    #events = collection.find({}).sort('date',1) #ascending order
    events = collection.find({}).sort('date',-1) #descending order
    return render_template('index.html', events = events)


# CONNECT TO DB, ADD DATA

@app.route('/add')

def add():
    # connect to the database
    user=mongo.db.users
    # insert new data
    user.insert({"name":"Mario"})
    # return a message to the user
    return "add user"

@app.route('/events/new', methods=['GET','POST'])

def new_event():
    if request.method=="GET":
        return render_template('new_event.html')
    else:
        event_name = request.form['event_name']
        event_date = request.form['event_date']
        user_name = request.form['user_name']

        events = mongo.db.events

        events.insert({'event':event_name,'date':event_date,"user":user_name})
        return redirect('/')
