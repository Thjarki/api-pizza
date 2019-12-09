import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from string import digits

myUrl = 'https://www.greifinn.is/pizza/index/pizza#center'


uClient = uReq(myUrl)

page_html = uClient.read()
uClient.close()


page_soup = soup(page_html, "html.parser")

pizzas = page_soup.find(id="pizzaMenu").findAll("li")

iterPizzas = iter(pizzas)
next(iterPizzas)

for pizza in iterPizzas:
	pizzaName = pizza.h4.text
	pizzaTopping =  pizza.div.text
	listPizzaTopping = pizzaTopping.split(", ")
	temp = pizza.find("div", {"class" : "price"}).findAll("div")[0].text
	pizzaSmallPrice = ''.join(i for i in temp if i.isdigit())
	temp = pizza.find("div", {"class" : "price"}).findAll("div")[1].text
	pizzaMidPrice = ''.join(i for i in temp if i.isdigit())
	temp = pizza.find("div", {"class" : "price"}).findAll("div")[2].text
	pizzaBigPrice = ''.join(i for i in temp if i.isdigit())

	print("Nafn : " + pizzaName )
	print("alegg : " + pizzaTopping)
	print(listPizzaTopping)
	print("litil verd: " + pizzaSmallPrice)
	print("midstared : " + pizzaMidPrice)
	print("stor verd : " + pizzaBigPrice)