from scraper import scrapedList

# do some kind of matching so that we only send scrapedList valid urls from DC site

# calendar valid days: 09/16 - 09/30
#                      10/01 - 10/31
#                      11/01 - 11/17

# ordered dict setup: https://i.imgur.com/KI8i9b5.png
dataset = []

for i in range(16, 31, 1): # only covers Wiley DC from 09/16 - 09/30
    returnVal_ScrapedList = scrapedList("https://dining.purdue.edu/menus/Wiley/2019/09/" + str(i) + "/Dinner")
    if not (returnVal_ScrapedList is None):
        dataset.append(returnVal_ScrapedList)


# append value mapped list into 2d dataset array