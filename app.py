import json
from db_operations import *
from sheduler_service import load_jobs
from flask import Flask
app = Flask(__name__)

@app.before_first_request
def init_scheduler():
    print("Jobs Will Be loaded shcheduler")
    load_jobs()

@app.route("/")
def hello():
    print("Calling request")
    db = DbOperations()
    cur = db.get_last_bid_ask()

    response = app.response_class(
        response=json.dumps(cur),
        status=200,
        mimetype='application/json'
    )
    return response




