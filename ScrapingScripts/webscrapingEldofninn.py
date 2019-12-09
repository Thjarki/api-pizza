import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from string import digits

myUrl = 'http://eldofninn.is/#matsedill'


uClient = uReq(myUrl)

page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

pizzas = page_soup.findAll("ul", {"class" : "av-catalogue-list"})[0].findAll("li")
pizzas += page_soup.findAll("ul", {"class" : "av-catalogue-list"})[1].findAll("li")

for pizza in pizzas:
	pizzaName = pizza.find("div", {"class" : "av-catalogue-title"}).text[4:].strip()
	pizzaTopping = pizza.find("div", {"class" : "av-catalogue-content"}).text.strip()
	listPizzaTopping = pizzaTopping.split(" – ")
	pizzaMidPrice = pizza.find("div", {"class" : "av-catalogue-price"}).text[14:19]

	print("Nafn : " + pizzaName )
	print("alegg : " + pizzaTopping)
	print(listPizzaTopping)
	print("midstared : " + pizzaMidPrice)