from flask import Flask, render_template, request

app = Flask(__name__, static_folder="public", static_url_path="")

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/add_device", methods=["GET", "POST"])
def add_device():
  if request.method == "POST":
    name = request.form["name"]
    type = request.form["type"]
    print(name, type)
  return render_template("add_device.html")

app.run('127.0.0.1', port = 5500, debug = True)