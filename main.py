from Scraper.ScraperF1 import ScraperF1
from Scraper.ScraperRT import ScraperRT


a = ScraperF1()

currency = a.extract_EUR_USD_Bid_Ask()

print("F1 currency")
print(currency)

a = ScraperRT()

currency = a.extract_EUR_USD_Bid_Ask()

print("RT currency")
print(currency)