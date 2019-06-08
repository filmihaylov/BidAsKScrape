from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from decimal import *
import time

class ScraperF1:

    def __init__(self):
        self.url = "https://1forge.com/forex-data-api/currency-pair-list"
        self.bid_ask = {"EUR": 0, "USD": 0}
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.get(self.url)


    def extract_EUR_USD_Bid_Ask(self):
        try:
            EUR = Decimal(self.get_EUR_bid().strip())
            USD = Decimal(self.get_USD_Bid().strip())
        except:
            self.driver.quit()
            raise Exception("String conversion to decimal failed EUR:" + self.get_EUR_bid().strip() + "USD:" + self.get_USD_Bid().strip())

        self.bid_ask["EUR"] = str(EUR)
        self.bid_ask["USD"] = str(USD)

        self.driver.quit()

        return self.bid_ask

    def get_EUR_bid(self):
        # late loading and too manny requests leads to connection refused
        time.sleep(10)
        try:
            element = self.driver.find_element(By.XPATH, "//tr[@class='base-EUR quote-USD']//span[@class='bid transition']")
            return element.text
        except:
            raise Exception("Element bid location changed on" + self.url)
    
    def get_USD_Bid(self):
        # late loading and too manny requests leads to connection refused:
        time.sleep(10)
        try:
            element = self.driver.find_element(By.XPATH, "//tr[@class='base-EUR quote-USD']//span[@class='ask transition']")
            return element.text
        except:
            raise Exception("Element ask location changed on" + self.url)