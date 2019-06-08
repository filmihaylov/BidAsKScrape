from flask import Flask
app = Flask(__name__)
import json

from Scraper.ScraperF1 import ScraperF1
from Scraper.ScraperRT import ScraperRT

from db_operations import *


@app.route("/")
def hello():
    #a = ScraperF1()

    #currency1 = a.extract_EUR_USD_Bid_Ask()

    #print("F1 currency")
    #print(currency1)

    a = ScraperRT()

    currency2 = a.extract_EUR_USD_Bid_Ask()

    print("RT currency")
    print(currency2)

    db = DbOperations()

    db.insert(currency2, "RT")

    cur = db.get_last_bid_ask()

    return str(cur)bid_ask_value




