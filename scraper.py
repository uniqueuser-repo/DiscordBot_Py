from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from collections import OrderedDict

def scrapedList(url_input):  # returns a value listing of matched foods or "NONE" if dining court is closed
    goods = ["orange chicken", "popcorn chicken", "breaded chicken tenders", "crispy pepperoni pizza", "hamburgers", "popcorn shrimp", "crispy meat lovers pizza", "sloppy joe",
             'made to order venetian pasta bar', "sloppy joe", "mini corn dogs", "steak house coulotte beef wiley", "clam strips", "spicy fried cheese ravioli", "meat lover's pizza",
             "tempura sweet & sour chicken", "macaroni shells and cheese", "fraldinha beef", "cream cheese wonton", "crispy jalapeno popper pizza", "crispy mac n cheese pizza",
             "fajita seasoned beef with vegetables", "general tso chicken", "hamburger", "mozzarella sticks", "macaroni & cheese", "crispy meat lovers pizza"]

    returnOrderedDict = OrderedDict() # key-value mapping OrderedDict

    for i in range(len(goods)): # map each food to an index, mark 0 for nonexistent
        returnOrderedDict[goods[i]] = 0


    url = url_input
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    html = driver.page_source

    if html.count("Bummer!"):
        return None              # returns "none" if the DC is closed that day


    soup = BeautifulSoup(html, 'html.parser')

    for element in soup.find_all('span', {'class':'station-item-text'}):
        elementString = str(element.contents[0].encode('utf-8'))
        elementString = elementString[2:-1]
        if goods.count(elementString.lower()) != 0:
            returnOrderedDict[elementString.lower()] = 1         # if the food exists at the dining court on that day, change the value of the food's mapping to 1.

    returnedList = []
    for i in range(len(returnOrderedDict)):
        returnedList.append(list(returnOrderedDict.items())[i][1])

    #driver.close()
    print()

    return returnedList