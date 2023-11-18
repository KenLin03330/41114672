import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

from flask import Flask, render_template, request
from datetime import datetime, timezone, timedelta

app = Flask(__name__)


@app.route("/")
def index():
    homepage = "<h1>林浚承的求職相關資訊</h1>"
    homepage += "<a href=/lin>我的個人簡介</a><br>"
    homepage += "<a href=/mis>MIS相關工作介紹</a><br>"
    homepage += "<a href=/him>求職履歷自傳</a><br>"
    return homepage

@app.route("/lin")
def lin():
    return render_template("lin.html")
@app.route("/mis")
def mis():
    return render_template("mis.html")
@app.route("/him")
def him():
    return render_template("him.html")

if __name__ == "__main__":
    app.run()
    #serve(app, host='0.0.0.0', port=8080)