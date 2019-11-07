from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from collections import OrderedDict

def scrapedList(url_input):  #returns a list of matched foods
    goods = ["orange chicken", "popcorn chicken", "breaded chicken tenders", "crispy pepperoni pizza", "hamburgers", "popcorn shrimp", "crispy meat lovers pizza", "sloppy joe",
             "made to order piedmont pasta bar", "sloppy joe", "mini corn dogs", "steak house coulotte beef wiley", "clam strips", "spicy fried cheese ravioli", "meat lover's pizza",
             "tempura sweet & sour chicken", "macaroni shells and cheese", "fraldinha beef", "cream cheese wonton", "crispy jalapeno popper pizza", "crispy mac n cheese pizza",
             "fajita seasoned beef with vegetables", "general tso chicken", "hamburger", "mozzarella sticks"]

    returnList = {}

    for i in range(len(goods)): # map each food to an index, mark 0 for nonexistent
        returnList[goods[i]] = 0


    url = url_input
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    html = driver.page_source


    soup = BeautifulSoup(html, 'html.parser')

    for element in soup.find_all('span', {'class':'station-item-text'}):
        elementString = str(element.contents[0].encode('utf-8'))
        elementString = elementString[2:-1]
        if goods.count(elementString.lower()) != 0:
            returnList[elementString] = 1         # if the food exists at the dining court on that day, change the value of the food's mapping to 1.

    return returnList

returnedDict = scrapedList("https://dining.purdue.edu/menus/Wiley/2019/11/7/Dinner/")

print("Done!")