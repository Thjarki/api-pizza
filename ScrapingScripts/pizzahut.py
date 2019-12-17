import bs4
import re
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from string import digits

myUrl = 'https://www.pizzahut.is/categories/pizzur?sc_pref_tags_not_in=dine_in_only'
uClient = uReq(myUrl)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")


containers = page_soup.findAll("div", {"class": "product"})

# first 2 containers are not pizzas and are therefore skipped.
print(str(len(containers)-2) + " pizzas parsed")

for container in containers[2:]:
    name = container.div.form.findAll("div", {"class": "product__top"})[0].h4.div.text
    price = re.findall('\d+', container.div.form.findAll("div", {"class": "product__mobile-price"})[0].findAll("div", {"class": "product__mobile-price-value"})[0].text)[0]

    print(name.strip() + ": " + str(price) + "kr.")
