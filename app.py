from flask import Flask, jsonify, render_template
import json
import os
from dotenv import load_dotenv
from pymongo import MongoClient

app = Flask(__name__)

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
print(MONGO_URI)

client = MongoClient(MONGO_URI)

client.admin.command("ping")
print("MongoDB connected successfully!")

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



