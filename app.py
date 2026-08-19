from flask import Flask, jsonify, render_template
import json

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/api")
def api():
    with open("data.json", "r") as file:
        data = json.load(file)
    return jsonify(data)

@app.route("/form")
def form():
    return render_template("form.html")

if __name__=="__main__":
    app.run()


