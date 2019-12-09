import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from string import digits

myUrl = 'https://castello.is/matsedill/#pizza'


uClient = uReq(myUrl)

page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

pizzas = page_soup.findAll("div", {"class" : "wppizza-article-info"})
pizzasPrice = page_soup.findAll("div", {"class" : "clearfix wppizza-article-tiers wppizza-article-prices-1"})
listi = []
i = 0
k = 0
for pizza in pizzas[:28]:
	if k == 1:
		k += 1
		continue
	pizzaName = pizza.h2.text.strip()
	pizzaTopping = pizza.p.text.split('\n')[0]
	listPizzaTopping = pizzaTopping.split(", ")
	try:
		pizzaSmallPrice = pizzasPrice[i].findAll("span")[1].text.strip()
	except:
		pizzaSmallPrice = ""
	try:
		pizzaMidPrice = pizzasPrice[i].findAll("span")[3].text.strip()
	except:
		pizzaMidPrice = ""
	try:
		pizzaBigPrice = pizzasPrice[i].findAll("span")[5].text.strip()
	except:
		pizzaBigPrice = ""
	i += 1
	k += 1

	print("Nafn : " + pizzaName )
	print("alegg : " + pizzaTopping)
	print(listPizzaTopping)
	print("litil verd: " + pizzaSmallPrice)
	print("midstared : " + pizzaMidPrice)
	print("stor verd : " + pizzaBigPrice)	

#virkar en má gera miklu betur, þetta tekur ekki eftirréttar pizzur og ekki kebab pizzur