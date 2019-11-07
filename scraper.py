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

for element in soup.find_all('span', {'class':'station-item-text'}):
    print(str(element.contents))