import requests
from bs4 import BeautifulSoup
import app.Scrapes.scrapeMananger as ScrapeManager

URL = 'http://eldofninn.is/#matsedill'


# TODO: Test
def scrape_eldofninn():
	page = requests.get(URL)
	soup = BeautifulSoup(page.content, "html.parser")

	pizzas = soup.findAll("ul", {"class": "av-catalogue-list"})[0].findAll("li")
	pizzas += soup.findAll("ul", {"class": "av-catalogue-list"})[1].findAll("li")
	company_id = ScrapeManager.insert_or_get_company(name='Eldofninn', region='höfuðborgarsvæðið', delivers=False).id

	for pizza in pizzas:
		pizzaName = pizza.find("div", {"class": "av-catalogue-title"}).text[4:].strip()
		pizzaTopping = pizza.find("div", {"class": "av-catalogue-content"}).text.strip().lower()
		listPizzaTopping = pizzaTopping.split(" – ")
		pizzaMidPrice = pizza.find("div", {"class": "av-catalogue-price"}).text[14:19]

		# Don't add when pizza exists, TODO: Update pizza
		if ScrapeManager.pizza_exists(pizzaName, company_id):
			continue
		ScrapeManager.add_scraped_pizza(pizzaName, listPizzaTopping, company_id, m_price=pizzaMidPrice)
