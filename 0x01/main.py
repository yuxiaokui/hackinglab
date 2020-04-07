from flask import Flask
app = Flask(__name__)

@app.route("/")
def ctf():
    return "<script>location='error'</script> Flag{302 is good!}"

@app.route("/error/")
def error():
    return "Error!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
