import schedule
from datetime import datetime, timedelta
from scraper import scrapedList
import pandas as pd
from dotenv import load_dotenv
import os
import ast
import time

load_dotenv()

def scrapeFour():
    print("RUNNING!\n\n\n\n")
    three_days_ahead = datetime.now() + timedelta(days=3)

    ongoing_dataframe = pd.read_csv(os.getenv("ONGOING_LIST"))

    for index, row in ongoing_dataframe.iterrows():
        element = ast.literal_eval(row['0'])
        if str(element[0]) + "/" + str(element[1]) + "/" + str(element[2]) == three_days_ahead.strftime("%Y/%m%d"):
            return

    yearVal = three_days_ahead.year
    monthVal = three_days_ahead.month
    dayVal = three_days_ahead.day

    wileyScraped, wileyFoodScraped = scrapedList("https://dining.purdue.edu/menus/Wiley/" + str(yearVal) + "/" + str(monthVal).zfill(2) + "/" + str(dayVal).zfill(2) + "/Dinner")
    hillenbrandScraped, hillenbrandFoodScraped = scrapedList("https://dining.purdue.edu/menus/Hillenbrand/" + str(yearVal) + "/" + str(monthVal).zfill(2) + "/" + str(dayVal).zfill(2) + "/Dinner")
    windsorScraped, windsorFoodScraped = scrapedList("https://dining.purdue.edu/menus/Windsor/" + str(yearVal) + "/" + str(monthVal).zfill(2) + "/" + str(dayVal).zfill(2) + "/Dinner")
    fordScraped, fordFoodScraped = scrapedList("https://dining.purdue.edu/menus/Ford/" + str(yearVal) + "/" + str(monthVal).zfill(2) + "/" + str(dayVal).zfill(2) + "/Dinner")
    dataset = [[[yearVal, monthVal, dayVal, [wileyScraped, wileyFoodScraped]]]]
    dataset.append([[yearVal, monthVal, dayVal, [hillenbrandScraped, hillenbrandFoodScraped]]])
    dataset.append([[yearVal, monthVal, dayVal, [windsorScraped, windsorFoodScraped]]])
    dataset.append([[yearVal, monthVal, dayVal, [fordScraped, fordFoodScraped]]])

    generated_dataframe = pd.DataFrame(dataset, columns=['0'])
    ongoing_dataframe = ongoing_dataframe.drop(ongoing_dataframe.columns[0], axis=1)
    ongoing_dataframe = ongoing_dataframe.append(generated_dataframe, ignore_index=True)
    ongoing_dataframe.to_csv(os.getenv("ONGOING_LIST"))


schedule.every().day.at("00:00").do(scrapeFour)

while (1):
    now = datetime.now()
    print(str(now))
    schedule.run_pending()
    time.sleep(1800)
