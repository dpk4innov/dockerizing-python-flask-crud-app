from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
app = Flask(__name__)

# Configure db
#db = yaml.load(open('db.yaml'))
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_HOST'] = 'db'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] ='dP@34'
app.config['MYSQL_DB'] = 'docker'

mysql = MySQL(app)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST'and 'submit' in request.form:
        # Fetch form data
        userDetails = request.form
        id1= userDetails['id']
        name= userDetails['name']
        age=userDetails['age']
        dep=userDetails['dep']
        sub=userDetails['sub']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO user(ID,Name,Age,Department,Subject) VALUES(%s, %s,%s,%s,%s)",(id1,name,age,dep,sub))
        mysql.connection.commit()
        cur.close()
        return redirect('/users')
    elif request.method == 'POST'and 'update' in request.form:
        # Fetch form data
        userDetails = request.form
        id1= userDetails['id']
        name= userDetails['name']
        age=userDetails['age']
        dep=userDetails['dep']
        sub=userDetails['sub']
        cur = mysql.connection.cursor()
        cur.execute("update user set Name=%s,Age=%s,Department=%s,Subject=%s where ID=%s",(name,age,dep,sub,id1))
        mysql.connection.commit()
        cur.close()
        return redirect('/users')
    elif request.method == 'POST'and 'delete' in request.form:
        userDetails = request.form
        id1= userDetails['id']
        cur = mysql.connection.cursor()
        cur.execute("delete from user where ID=%s",(id1,))
        mysql.connection.commit()
        cur.close()
        return redirect('/users')
    return render_template('index.html')

@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM user")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('users.html',userDetails=userDetails)

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
