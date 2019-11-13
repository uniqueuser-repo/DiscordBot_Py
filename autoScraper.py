import schedule
from datetime import datetime, timedelta
from scraper import scrapedList
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

def scrapeFour():
    seven_days_ahead = datetime.now() + timedelta(days=1)

    yearVal = seven_days_ahead.year
    monthVal = seven_days_ahead.month
    dayVal = seven_days_ahead.day

    wileyScraped, wileyFoodScraped = scrapedList("https://dining.purdue.edu/menus/Wiley/" + str(yearVal) + "/" + str(monthVal).zfill(2) + "/" + str(dayVal).zfill(2) + "/Dinner")
    hillenbrandScraped, hillenbrandFoodScraped = scrapedList("https://dining.purdue.edu/menus/Hillenbrand/" + str(yearVal) + "/" + str(monthVal).zfill(2) + "/" + str(dayVal).zfill(2) + "/Dinner")
    windsorScraped, windsorFoodScraped = scrapedList("https://dining.purdue.edu/menus/Windsor/" + str(yearVal) + "/" + str(monthVal).zfill(2) + "/" + str(dayVal).zfill(2) + "/Dinner")
    fordScraped, fordFoodScraped = scrapedList("https://dining.purdue.edu/menus/Ford/" + str(yearVal) + "/" + str(monthVal).zfill(2) + "/" + str(dayVal).zfill(2) + "/Dinner")

    dataset = pd.read_csv(os.getenv("ONGOING_LIST"))

    generated_dataframe = pd.DataFrame(dataset)
    generated_dataframe.append([[[yearVal, monthVal, dayVal, [wileyScraped, wileyFoodScraped]]]])
    generated_dataframe.append([[yearVal, monthVal, dayVal, [hillenbrandScraped, hillenbrandFoodScraped]]])
    generated_dataframe.append([[yearVal, monthVal, dayVal, [windsorScraped, windsorFoodScraped]]])
    generated_dataframe.append([[yearVal, monthVal, dayVal, [fordScraped, fordFoodScraped]]])

    generated_dataframe.to_csv(os.getenv("ONGOING_LIST"))



scrapeFour()
#schedule.every().day.at("00:00").do(scrapeFour())