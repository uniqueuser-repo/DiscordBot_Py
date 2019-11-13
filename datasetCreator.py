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
    returnVal_ScrapedList = scrapedList("https://dining.purdue.edu/menus/" + diningCourt + "/2019/" + str(month).zfill(2) + "/" + str(day).zfill(2) + "/Dinner")
    if not (returnVal_ScrapedList is None):
        dataset.append(returnVal_ScrapedList)


dataset = []

for day in range(16, 31, 1):               # covers Wiley, Hillenbrand, Ford, Windsor DC from 09/16 - 09/30
    scrapeDiningCourt("Wiley", day, 9)
    scrapeDiningCourt("Hillenbrand", day, 9)
    scrapeDiningCourt("Ford", day, 9)
    scrapeDiningCourt("Windsor", day, 9)

for day in range(1, 32, 1):                # covers Wiley, Hillenbrand, Ford, Windsor DC from 10/01 - 10/31
    scrapeDiningCourt("Wiley", day, 10)
    scrapeDiningCourt("Hillenbrand", day, 10)
    scrapeDiningCourt("Ford", day, 10)
    scrapeDiningCourt("Windsor", day, 10)

for day in range(1, 18, 1):
    scrapeDiningCourt("Wiley", day, 11)
    scrapeDiningCourt("Hillenbrand", day, 11)
    scrapeDiningCourt("Ford", day, 11)
    scrapeDiningCourt("Windsor", day, 11)

dataset_to_pandas = pd.DataFrame.from_records(dataset)

load_dotenv()
OUTPUTFILE_PATH = os.getenv('OUTPUTFILE_PATH')

dataset_to_pandas.to_csv(OUTPUTFILE_PATH)







