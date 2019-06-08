import time
from apscheduler.schedulers.background import BackgroundScheduler
from Scraper.ScraperF1 import ScraperF1
from Scraper.ScraperRT import ScraperRT

from db_operations import *

def save_bid_ask_scheduler():
    print("Task For save Bid Ask scheduler started")
    try:
        rt_scraper = ScraperRT()
        bid_ask_pair = rt_scraper.extract_EUR_USD_Bid_Ask()
        db = DbOperations()
        db.insert(bid_ask_pair, "RT")
    except:
        f1_scraper = ScraperF1()
        bid_ask_pair = f1_scraper.extract_EUR_USD_Bid_Ask()
        db = DbOperations()
        db.insert(bid_ask_pair, "F1")


def clear_old_data_scheduler():
    print("Task For DELETE Bid Ask scheduler started")
    db = DbOperations()
    db.delete_old_data()


def load_jobs():
    sched_save_bid_ask = BackgroundScheduler()
    sched_save_bid_ask.add_job(save_bid_ask_scheduler, 'interval', minutes=2)
    sched_save_bid_ask.start()
    print("Task For starting function save Bid Ask scheduler started")

    sched_clear_old_data = BackgroundScheduler()
    sched_clear_old_data.add_job(clear_old_data_scheduler, 'interval', minutes=2)
    sched_clear_old_data.start()
    print("Task For starting function DELETE Bid Ask scheduler started")
