import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from string import digits

myUrl = 'https://www.pizzasmidjan.is/is/matsedlar/matsedill'


uClient = uReq(myUrl)

page_html = uClient.read()
uClient.close()


page_soup = soup(page_html, "html.parser")

pizzas = page_soup.findAll("div", {"class" : "item"})


for pizza in pizzas:
	pizzaName = pizza.find("div",{"class", "item_title"}).text.strip()
	pizzaTopping = pizza.find("div",{"class", "item_desc"}).text.strip()
	pizzaMidPrice = pizza.find("div",{"class", "item_price"}).text.strip()[5:10]

	print("Nafn : " + pizzaName )
	print("alegg : " + pizzaTopping)
	print("midstared : " + pizzaMidPrice)