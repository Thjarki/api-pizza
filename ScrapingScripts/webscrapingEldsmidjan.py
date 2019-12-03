import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from string import digits

myUrl = 'https://www.eldsmidjan.is/#/'


uClient = uReq(myUrl)

page_html = uClient.read()
uClient.close()


page_soup = soup(page_html, "html.parser")

pizzas = page_soup.findAll("div", {"class":"grid product pizza"})
pizzas += page_soup.findAll("div", {"class":"grid product pizza best-seller"})
pizzas += page_soup.findAll("div", {"class":"grid product pizza vegetarian"})
pizzas += page_soup.findAll("div", {"class":"grid product pizza vegetarian best-seller"})

for pizza in pizzas:
	temp = pizza.h3.text.replace("\r", "").replace("\t", "").replace("\n", "").replace("E1", "").replace("E2", "")
	pizzaName = ''.join(i for i in temp if not i.isdigit())
	pizzaTopping = pizza.p.text.strip()
	pizzaMidPrice = pizza.li.text.replace("\r", "").replace("\t", "").replace("\n", "").replace("+", "")[3:]
	pizzaBigPrice = pizza.findAll("li")[1].text.replace("\r", "").replace("\t", "").replace("\n", "").replace("+", "")[4:]


	print("Nafn : " + pizzaName )
	print("alegg : " + pizzaTopping)
	print("midstared : " + pizzaMidsizePrice)
	print("stor verd : " + pizzaBigsizePrice)

#þessi web scraper tekur bara pizzur ekki tilboð