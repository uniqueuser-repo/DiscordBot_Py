from scraper import scrapedList
import pandas as pd

# do some kind of matching so that we only send scrapedList valid urls from DC site

# calendar valid days: 09/16 - 09/30
#                      10/01 - 10/31
#                      11/01 - 11/17

# ordered dict setup: https://i.imgur.com/KI8i9b5.png

dataset = []

def scrapeDiningCourt(diningCourt, i, month):
    returnVal_ScrapedList = scrapedList("https://dining.purdue.edu/menus/" + diningCourt + "/2019/" + str(month).zfill(2) + "/" + str(i).zfill(2) + "/Dinner")
    if not (returnVal_ScrapedList is None):
        dataset.append(returnVal_ScrapedList)


for i in range(16, 31, 1):               # covers Wiley, Hillenbrand, Ford, Windsor DC from 09/16 - 09/30
    scrapeDiningCourt("Wiley", i, 9)
    scrapeDiningCourt("Hillenbrand", i, 9)
    scrapeDiningCourt("Ford", i, 9)
    scrapeDiningCourt("Windsor", i, 9)

for i in range(1, 32, 1):                # covers Wiley, Hillenbrand, Ford, Windsor DC from 10/01 - 10/31
    scrapeDiningCourt("Wiley", i, 10)
    scrapeDiningCourt("Hillenbrand", i, 10)
    scrapeDiningCourt("Ford", i, 10)
    scrapeDiningCourt("Windsor", i, 10)

for i in range(1, 18, 1):
    scrapeDiningCourt("Wiley", i, 11)
    scrapeDiningCourt("Hillenbrand", i, 11)
    scrapeDiningCourt("Ford", i, 11)
    scrapeDiningCourt("Windsor", i, 11)

dataset_to_pandas = pd.DataFrame.from_records(dataset)

dataset_to_pandas.to_csv(r"C:\Users\Andy\PycharmProjects\DiscordBot_Py\outputfile.csv")





