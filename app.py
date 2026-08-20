from flask import Flask, jsonify, render_template, request, redirect, url_for
import json
import os
from dotenv import load_dotenv
from pymongo import MongoClient

app = Flask(__name__)

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")


client = MongoClient(MONGO_URI)

db = client["flask_database"]
collection = db["submissions"]


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

@app.route("/success")
def success():
    return render_template("success.html")


@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    email = request.form.get("email")

    if not name or not email:
        error = "Name and email are required."
        return render_template("form.html", error=error)

    try:
        collection.insert_one({
            "name": name,
            "email": email
        })
    except Exception:
        error = "Failed to submit data. Please try again."
        return render_template("form.html", error=error)

    return redirect(url_for("success"))

if __name__=="__main__":
    app.run()



