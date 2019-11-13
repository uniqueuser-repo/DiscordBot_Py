import schedule
from datetime import datetime, timedelta
from scraper import scrapedList
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

def scrapeFour():
    print("RUNNING!\n\n\n\n")
    seven_days_ahead = datetime.now() + timedelta(days=3)

    yearVal = seven_days_ahead.year
    monthVal = seven_days_ahead.month
    dayVal = seven_days_ahead.day

    wileyScraped, wileyFoodScraped = scrapedList("https://dining.purdue.edu/menus/Wiley/" + str(yearVal) + "/" + str(monthVal).zfill(2) + "/" + str(dayVal).zfill(2) + "/Dinner")
    hillenbrandScraped, hillenbrandFoodScraped = scrapedList("https://dining.purdue.edu/menus/Hillenbrand/" + str(yearVal) + "/" + str(monthVal).zfill(2) + "/" + str(dayVal).zfill(2) + "/Dinner")
    windsorScraped, windsorFoodScraped = scrapedList("https://dining.purdue.edu/menus/Windsor/" + str(yearVal) + "/" + str(monthVal).zfill(2) + "/" + str(dayVal).zfill(2) + "/Dinner")
    fordScraped, fordFoodScraped = scrapedList("https://dining.purdue.edu/menus/Ford/" + str(yearVal) + "/" + str(monthVal).zfill(2) + "/" + str(dayVal).zfill(2) + "/Dinner")
    dataset = [[[yearVal, monthVal, dayVal, [wileyScraped, wileyFoodScraped]]]]
    dataset.append([[yearVal, monthVal, dayVal, [hillenbrandScraped, hillenbrandFoodScraped]]])
    dataset.append([[yearVal, monthVal, dayVal, [windsorScraped, windsorFoodScraped]]])
    dataset.append([[yearVal, monthVal, dayVal, [fordScraped, fordFoodScraped]]])

    generated_dataframe = pd.DataFrame(dataset, columns=['0'])
    ongoing_dataframe = pd.read_csv(os.getenv("ONGOING_LIST"))
    ongoing_dataframe = ongoing_dataframe.drop(ongoing_dataframe.columns[0], axis=1)
    ongoing_dataframe = ongoing_dataframe.append(generated_dataframe, ignore_index=True)
    ongoing_dataframe.to_csv(os.getenv("ONGOING_LIST"))


schedule.every(1).day.at("00:00").do(scrapeFour)

while (1):
    schedule.run_pending()

