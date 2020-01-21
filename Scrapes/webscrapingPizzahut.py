import requests
import re
from bs4 import BeautifulSoup
from string import digits

# Only small size can be scraped and the menu is split up in two locations and whether you are picking up or delivery.

URL = 'https://www.pizzahut.is/categories/pizzur?sc_pref_tags_not_in=dine_in_only'
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

containers = soup.findAll("div", {"class": "product"})

# first 2 containers are not pizzas and are therefore skipped.
print(str(len(containers)-2) + " pizzas parsed")

for container in containers[2:]:
    name = container.div.form.findAll("div", {"class": "product__top"})[0].h4.div.text
    price = re.findall('\d+', container.div.form.findAll("div", {"class": "product__mobile-price"})[0].findAll("div", {"class": "product__mobile-price-value"})[0].text)[0]

    print(name.strip() + ": " + str(price) + "kr.")
