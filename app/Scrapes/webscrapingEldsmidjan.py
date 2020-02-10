import requests
import app.Scrapes.scrapeMananger as ScrapeManager
from bs4 import BeautifulSoup
import re

URL = 'https://www.eldsmidjan.is/#/'


# TODO: create Test and error handling
def scrape_eldsmidjan():
	try:
		page = requests.get(URL)
	except requests.Timeout:
		# TODO: notify of this error
		return
	soup = BeautifulSoup(page.content, "html.parser")

	pizza_elms = soup.findAll("div", {"class": "pizza"})

	company_id = ScrapeManager.insert_or_get_company(name='Eldsmiðjan', region='höfuðborgarsvæðið', delivers=True).id

	for pizza in pizza_elms:
		pizza.h3.span.replace_with('')
		pizzaName = re.sub(r'[^ \w\.]', '', pizza.h3.text)
		pizzaTopping = pizza.p.text.strip().lower()
		listPizzaTopping = pizzaTopping.split(", ")
		pizzaMidPrice = None
		pizzaBigPrice = None

		price = soup.find('div', string="Mið").parent.text
		if price is not None:
			pizzaMidPrice = re.sub(r"\D", "", price)

		price = soup.find('div', string="Stór").parent.text
		if price is not None:
			pizzaBigPrice = re.sub(r"\D", "", price)

		#print("Nafn: {}".format(pizzaName))
		#print("alegg: {}".format(pizzaTopping))
		#print(listPizzaTopping)
		#print("litil verd: {}".format(None))
		#print("midstared: {}".format(pizzaMidPrice))
		#print("stor verd: {}".format(pizzaBigPrice))

		ScrapeManager.add_scraped_pizza(pizzaName, listPizzaTopping, company_id, m_price=pizzaMidPrice, l_price=pizzaBigPrice)



