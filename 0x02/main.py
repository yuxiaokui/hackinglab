from flask import Flask,request
from urllib import unquote
import requests

app = Flask(__name__)

@app.route("/")
def ctf():
    return '''
    <form action='/save' method='POST'>
    Send to admin:<input name='text'>
    </form>
    '''

@app.route("/save",methods = ['POST'])
def save():
    data = request.get_data()
    data = unquote(data.decode())
    import re
    s = re.findall(r'//(.*?)\/',data)
    url = s[0]
    requests.get('http://' + url + '/?flag=Xi4okvIsHacker!' )
    return 'OK'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
