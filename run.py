from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "Welcome to VarIoT"

app.run('127.0.0.1', port = 5500, debug = True)