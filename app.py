
import flask
from sql_connection import get_sql_connection
from flask import app, session,redirect,request,url_for
import mysql.connector
import datetime
from flask import render_template


def get_sql_connection():
  print("Opening mysql connection")
  _connec = mysql.connector.connect(user='root', password='User@352001', database='grocery_store')

  

cursor = mysql.connect().cursor()
app = flask(__name__)
app.secret_key= "super secret key"


@app.route('/')
def index():
  return render_template('/Home page/register.html')

@app.route('/home')
def home():
  return render_template('index.html', username=-session['username'])



@app.route('/login', methods=['GET','POST'])
def login():
  mdg=''
  if request.method=='POST':
    username=request.form['username']
    password=request.form['password']
    cursor.execute('SELECT * FROM users WHERE username=%s AND password=%s',(username,password))
    record=cursor.fetchone()
    if record:
      session['loggedin']=True
      session['username']=record[1]
      return redirect(url_for('admin'))

    else:
      msg='Incorrect username/password. Try again !'
  return render_template('register.html',msg=msg)
