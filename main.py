from Scraper.ScraperRT import ScraperRT


a = ScraperRT()

currency = a.extract_EUR_USD_Bid_Ask()

print(currency)