import os
from flask import Flask, render_template, request, json, current_app as app

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

@app.route("/api/show_questions/<string:type>")
def api_show_questions(type):
  filename = os.path.join(app.static_folder, "json", type+ "_questions.json")
  with open(filename) as f:
    questions = json.load(f)
  print(questions)
  f.close()
  return questions

if __name__ == "__main__":
  app.run('127.0.0.1', port = 5500, debug = True)