import time
from apscheduler.schedulers.background import BackgroundScheduler
from Scraper.ScraperF1 import ScraperF1
from Scraper.ScraperRT import ScraperRT
import logging
from db_operations import *
from telegram_logging import send

logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='bid_ask.log',
                    filemode='w')

def save_bid_ask_scheduler():
    print("Task For save Bid Ask scheduler started")
    try:
        rt_scraper = ScraperRT()
        bid_ask_pair = rt_scraper.extract_EUR_USD_Bid_Ask()
        db = DbOperations()
        db.insert(bid_ask_pair, "RT")
    except Exception as e:
        logging.exception("fail in bid ask scheduler RT")
        send("fail in bid ask scheduler RT")

        try:
            f1_scraper = ScraperF1()
            bid_ask_pair = f1_scraper.extract_EUR_USD_Bid_Ask()
            db = DbOperations()
            db.insert(bid_ask_pair, "F1")
        except Exception as e:
            logging.exception("fail in bid ask scheduler F1 both sources failed all data in db will be cleared")
            # Very bad clear data in order to avoid false information
            db.delete_all()
            send("fail in bid ask scheduler F1 both sources failed all data in db will be cleared")
            raise e


def clear_old_data_scheduler():
    print("Task For DELETE Bid Ask scheduler started")
    try:
        db = DbOperations()
        db.delete_old_data()
    except Exception as e:
        logging.exception("fail in delete last five days data")
        send("fail in delete last five days data")
        raise e


def load_jobs():
    sched_save_bid_ask = BackgroundScheduler()
    sched_save_bid_ask.add_job(save_bid_ask_scheduler, 'interval', minutes=2)
    sched_save_bid_ask.start()
    print("Task For starting function save Bid Ask scheduler started")

    sched_clear_old_data = BackgroundScheduler()
    sched_clear_old_data.add_job(clear_old_data_scheduler, 'interval', minutes=5)
    sched_clear_old_data.start()
    print("Task For starting function DELETE Bid Ask scheduler started")
