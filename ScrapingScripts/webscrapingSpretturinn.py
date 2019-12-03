import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from string import digits

myUrl = 'http://www.spretturinn.is/is/pizzulisti'


uClient = uReq(myUrl)

page_html = uClient.read()
uClient.close()


page_soup = soup(page_html, "html.parser")

pizzas = page_soup.findAll("div", {"class":"tile product image"})

for pizza in pizzas:
	pizzaName = pizza.h2.text
	pizzaTopping = pizza.findAll("div", {"class":"description"})[0].text
	pizzaSmallPrice = pizza.findAll("span", {"class":"price"})[0].text
	pizzaMidPrice = pizza.findAll("span", {"class":"price"})[1].text
	pizzaBigPrice = pizza.findAll("span", {"class":"price"})[2].text

	print("Nafn : " + pizzaName )
	print("alegg : " + pizzaTopping)
	print("litil verd: " + pizzaSmallPrice)
	print("midstared : " + pizzaMidPrice)
	print("stor verd : " + pizzaBigPrice)