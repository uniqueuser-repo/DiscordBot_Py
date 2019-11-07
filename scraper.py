from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import time

url = "https://dining.purdue.edu/menus/Wiley/2019/11/7/"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
html = driver.page_source

#print("len html = " + str(len(html)))
#print("html = " + html)

soup = BeautifulSoup(html, 'html.parser')

#print("len soup = " + str(len(soup)))
#print("soup = " + str(soup))

goods = ["orange chicken", "popcorn chicken", "breaded chicken tenders", "crispy pepperoni pizza", "hamburgers", "popcorn shrimp", "crispy meat lovers pizza", "sloppy joe",
         "made to order piedmont pasta bar", "sloppy joe", "mini corn dogs", "steak house coulotte beef wiley", "clam strips", "spicy fried cheese ravioli", "meat lover's pizza",
         "tempura sweet & sour chicken", "macaroni shells and cheese", "fraldinha beef", "cream cheese wonton", "crispy jalapeno popper pizza", "crispy mac n cheese pizza",
         "fajita seasoned beef with vegetables", "general tso chicken", "hamburger", "mozzarella sticks"]

print("a")
for element in soup.find_all('span', {'class':'station-item-text'}):
    elementString = str(element.contents[0].encode('utf-8'))
    elementString = elementString[2:-1]
    #print(elementString.lower())
    #print("Type: " + str(type(elementString.lower())))
    var = goods.count(elementString.lower())
    if goods.count(elementString.lower()) != 0:
        print("FOUND! " + elementString)