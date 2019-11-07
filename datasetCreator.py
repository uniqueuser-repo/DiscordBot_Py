from scraper import scrapedList

# do some kind of matching so that we only send scrapedList valid urls from DC site

# calendar valid days: 09/16 - 09/30
#                      10/01 - 10/31
#                      11/01 - 11/17
dataset = []

for i in range(16, 31, 1): # only covers Wiley DC from 09/16 - 09/30
     dataset.append(scrapedList("https://dining.purdue.edu/menus/Wiley/2019/09/" + str(i) + "/Dinner"))


# append value mapped list into 2d dataset array