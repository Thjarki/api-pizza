from selenium import webdriver
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as BeautifulSoup
from string import digits
import time
from selenium.webdriver.support.ui import WebDriverWait

pause = 0

driver = webdriver.Firefox()

driver.get('https://shakepizza.is/matsedill/pizzur/')
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
##driver.implicitly_wait(5000)
time.sleep(pause)


html = driver.page_source
soup2 = BeautifulSoup(html, "html5lib")



soup = BeautifulSoup(driver.page_source, 'html.parser')
pizzas = soup2.findAll("div", {"class":"pizza_card"})
pizzaNames = soup2.findAll("div", {"class":"lazy-load-background"})

for pizza in pizzas:
	tempPizzaName = pizza.find("div", {"class":"lazy-load-background"})
	temp = tempPizzaName["data-style"].replace("url(https://shakepizza.is/wp-content/uploads/", "").replace("/", "").replace("-", " ").replace(".jpg", "").replace(".png", "").replace("x", "").replace(".jpeg", "").replace(")", "").replace("background image:", "").replace("wb", "").replace("_", " ").strip()
	pizzaName = ''.join(i for i in temp if not i.isdigit())
	pizzaMidPrice = pizza.span.text.strip()
	pizzaTopping = pizza.p.text.strip()

	print(pizzaName)
	print(pizzaTopping)
	print(pizzaMidPrice)



#pizzaName = driver.find_elements_by_xpath('//div[@class="grid-item  pizza_card"]')

#pizzapoop = pizzaName[1].get_attribute('innerHTML')
driver.close()