from flask import Flask,request
from urllib.parse import unquote
import requests
import sqlite3



app = Flask(__name__)

@app.route("/")
def ctf():
    return '''
    <form action='/login' method='POST'>
    password:<input name='password'>
    </form>
    '''

@app.route("/login",methods = ['POST'])
def save():
    conn = sqlite3.connect('db.db')
    c = conn.cursor()
    try:
        password = request.form['password']
        sql = 'select username from admin where password = ' + password
        cursor = c.execute(sql)
        for row in cursor:
            return "Welcome " + str(row[0])

    except Exception as e:
        #print(e)
        return 'Error'

    finally:
        c.close()
    


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
