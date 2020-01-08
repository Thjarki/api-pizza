import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from string import digits
from Model import Pizza, Price, Topping, db





def scrapePizzamiðjan():
	myUrl = 'https://www.pizzasmidjan.is/is/matsedlar/matsedill'

	uClient = uReq(myUrl)
	page_html = uClient.read()
	uClient.close()

	page_soup = soup(page_html, "html.parser")

	pizzas = page_soup.findAll("div", {"class": "item"})

	result = []

	for pizza in pizzas:
		pizzaName = pizza.find("div", {"class", "item_title"}).text.strip()
		pizzaTopping = pizza.find("div", {"class", "item_desc"}).text.strip()
		listPizzaTopping = pizzaTopping.split(", ")
		pizzaMidPrice = pizza.find("div", {"class", "item_price"}).text.strip()[5:10]

		# print("Nafn : " + pizzaName )
		# print("alegg : " + pizzaTopping)
		# print(listPizzaTopping)
		# print("midstared : " + pizzaMidPrice)

		# result.append(Pizza(pizzaName, pizzaTopping, listPizzaTopping, "m", pizzaMidPrice))

		toplist = []

		for item in listPizzaTopping:
			t = db.session.query(Topping).filter_by(name=item).first()
			if t is None:
				t = Topping(name=item)

			toplist.append(t)
		test = Price(size_m=int(pizzaMidPrice.replace('.', '')))
		p = Pizza(name=pizzaName, prices=test, toppings=toplist)
		# result.append(Pizza(name=pizzaName, prices=test, toppings=toplist))
		db.session.add(p)

	return
