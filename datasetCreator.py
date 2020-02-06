from scraper import scrapedList
import pandas as pd
import os
from dotenv import load_dotenv

# do some kind of matching so that we only send scrapedList valid urls from DC site

# calendar valid days: 09/16 - 09/30
#                      10/01 - 10/31
#                      11/01 - 11/17

# ordered dict setup: https://i.imgur.com/KI8i9b5.png

def scrapeDiningCourt(diningCourt, day, month):
    returnVal_ScrapedList = scrapedList("https://dining.purdue.edu/menus/" + diningCourt + "/2020/" + str(month).zfill(2) + "/" + str(day).zfill(2) + "/Dinner")
    returnVal_ScrapedList = returnVal_ScrapedList[0]
    if not (returnVal_ScrapedList is None):
        dataset.append(returnVal_ScrapedList)


dataset = []

for day in range(2, 12, 1):               # covers Wiley, Hillenbrand, Ford, Windsor DC from 12/02-12/11
    scrapeDiningCourt("Wiley", day, 12)
    scrapeDiningCourt("Hillenbrand", day, 12)
    scrapeDiningCourt("Ford", day, 12)
    scrapeDiningCourt("Windsor", day, 12)

for day in range(13, 32, 1):                # covers Wiley, Hillenbrand, Ford, Windsor DC from 01/13-01/31
    scrapeDiningCourt("Wiley", day, 1)
    scrapeDiningCourt("Hillenbrand", day, 1)
    scrapeDiningCourt("Ford", day, 1)
    scrapeDiningCourt("Windsor", day, 1)

for day in range(1, 7, 1):  # covers Wiley, Hillenbrand, Ford, Windsor DC from 02/01 - 02/06
    scrapeDiningCourt("Wiley", day, 2)
    scrapeDiningCourt("Hillenbrand", day, 2)
    scrapeDiningCourt("Ford", day, 2)
    scrapeDiningCourt("Windsor", day, 2)

dataset_to_pandas = pd.DataFrame.from_records(dataset)
dataset_to_pandas.index = dataset_to_pandas.index + 196

load_dotenv()
OUTPUTFILE_PATH = os.getenv('OUTPUTFILE_PATH')

dataset_to_pandas.to_csv(OUTPUTFILE_PATH, mode='a', header=False)







