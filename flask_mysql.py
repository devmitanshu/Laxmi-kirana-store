from flask import Flask,request,render_template
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='User@352001'
app.config['MYSQL_DATABASE_DB']='grocery_store'
app.config['MYSQL_DATABASE_HOST']='localhost'
mysql.init_app(app)

@app.route('/')
def my_form():
    return render_template('register.html')

@app.route('/',methods=['POST','GET'])
def Authenticate():
    username =request.form['username']
    password=request.form['password']
    cursor = mysql.connect().cursor()
    cursor.execute('SELECT * FROM admin WHERE username=%s AND password=%s',(username,password))
    data = cursor.fetchone()
    if data is None:
        return "Username or Password is wrong"
    else:
        return render_template('admin.html')


if __name__=="__main__":
    app.debug=True
    app.run()
