import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from string import digits

myUrl = 'http://wilsons.is/MenuSite.aspx?g=1200'


uClient = uReq(myUrl)

page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

pizzas = page_soup.findAll("div", {"class" : "bgWhite"})
iterpizzas = iter(pizzas)
next(iterpizzas)

for pizza in iterpizzas:
	pizzaName = pizza.span.text.replace(" m/20% afslætti", "").replace("Stór ", "").replace(" m/25% afslætti", "")
	pizzaTopping = pizza.find("span", {"class" : "aleggslysingText"}).text
	try:
		temp = pizza.findAll("option")[0].text[2:].replace("m/3", "").replace("Rocky 2", "") 
		pizzaBigPrice = ''.join(i for i in temp if i.isdigit())
	except:
		pizzaBigPrice = ""
	try:
		temp = pizza.findAll("option")[1].text[2:].replace("Rocky 2", "")  
		pizzaMidPrice = ''.join(i for i in temp if i.isdigit())
	except:
		pizzaMidPrice = ""
	try:
		temp = pizza.findAll("option")[2].text[2:].replace("Rocky 2", "") 
		pizzaSmallPrice = ''.join(i for i in temp if i.isdigit())
	except:
		pizzaSmallPrice = ""

	print("Nafn : " + pizzaName )
	print("alegg : " + pizzaTopping)
	print("litil verd: " + pizzaSmallPrice)
	print("midstared : " + pizzaMidPrice)
	print("stor verd : " + pizzaBigPrice)	