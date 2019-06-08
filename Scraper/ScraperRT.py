import requests
from Shared.PageGetter import simple_get
from bs4 import BeautifulSoup
from decimal import *

class ScraperRT:

    def __init__(self):
        self.url = "https://www.reuters.com/finance/currencies/quote?srcCurr=EUR&destCurr=USD"
        self.bid_ask = {"EUR": 0, "USD": 0}

    def extract_EUR_USD_Bid_Ask(self):
        html = BeautifulSoup(self.get_html(), 'html.parser')
        bids = html.find_all("div",class_="bidAsk")

        try:
            EUR = Decimal(self.get_EUR_bid(bids).strip())
            USD = Decimal(self.get_USD_Bid(bids).strip())
        except:
            raise Exception("String conversion to decimal failed EUR:" + self.get_EUR_bid(bids).strip() + "USD:" + self.get_USD_Bid(bids).strip())

        self.bid_ask["EUR"] = str(EUR)
        self.bid_ask["USD"] = str(USD)

        return self.bid_ask

    def get_html(self):
        data = simple_get(self.url)
        if data:
            return data
        else:
            raise Exception("Page Request Failed")

    def get_EUR_bid(self, soup):
        for element in soup:
            child = element.findChild()
            if "Bid" in child.get_text():
                return child.next_sibling.get_text()

    def get_USD_Bid(self, soup):
        for element in soup:
            child = element.findChild()
            if "Offer" in child.get_text():
                return child.next_sibling.get_text()