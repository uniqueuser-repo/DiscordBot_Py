from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from collections import OrderedDict
from selenium.webdriver.chrome.options import Options

def scrapedList(url_input):  # returns a value listing of matched foods or "NONE" if dining court is closed
    goods = ["orange chicken", "popcorn chicken", "breaded chicken tenders", "crispy pepperoni pizza", "hamburgers", "popcorn shrimp", "crispy meat lovers pizza", "sloppy joe",
             'made to order venetian pasta bar', "sloppy joe", "mini corn dogs", "steak house coulotte beef wiley", "clam strips", "spicy fried cheese ravioli", "meat lover's pizza",
             "tempura sweet & sour chicken", "macaroni shells and cheese", "fraldinha beef", "cream cheese wonton", "crispy jalapeno popper pizza", "crispy mac n cheese pizza",
             "fajita seasoned beef with vegetables", "general tso chicken", "hamburger", "mozzarella sticks", "macaroni & cheese", "crispy meat lovers pizza"]

    returnOrderedDict = OrderedDict() # key-value mapping OrderedDict

    for i in range(len(goods)): # map each food to an index, mark 0 for nonexistent
        returnOrderedDict[goods[i]] = 0

    #chrome_options = Options()                                         #
    #chrome_options.add_argument("--headless")                          # comment these lines to begin
    #chrome_options.add_argument("--window-size=%s" % "1920,1080")      # seeing the window again

    url = url_input
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    html = driver.page_source

    if html.count("Bummer!") or len(html) == 0 or html.lower().count("had a problem..") or html.lower().count("couldn't find that page"):
        driver.close()
        return None, "The dining court appears to be closed."              # returns "none" if the DC is closed that day


    soup = BeautifulSoup(html, 'html.parser')
    returnedFoodList = []


    var = soup.find_all('span', {'class':'station-item-text'})

    if (len(var) <= 1):
        return scrapedList(url_input) # if url was mishandled, re-call until it wasn't.

    for element in var:
        elementString = str(element.contents[0].encode('utf-8'))
        elementString = elementString[2:-1]
        elementStringLower = elementString.lower()
        if goods.count(elementString.lower()) != 0 or elementStringLower.count('piedmont'):
            if (elementStringLower.count('piedmont')):                     # different name, same thing
                returnOrderedDict['made to order venetian pasta bar'] = 1
                returnedFoodList.append(elementString.lower())
            else:
                returnOrderedDict[elementString.lower()] = 1          # if the food exists at the dining court on that day, change the value of the food's mapping to 1.
                returnedFoodList.append(elementString.lower())


    returnedList = []
    for i in range(len(returnOrderedDict)):
        returnedList.append(list(returnOrderedDict.items())[i][1])

    driver.close()
    print()

    return returnedList, returnedFoodList

