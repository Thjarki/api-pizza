from selenium import webdriver


driver = webdriver.Firefox()

driver.get('https://www.blackboxpizza.is/#Menu')

#pizzas = driver.find_elements_by_xpath('//div[@class="salescloud-product-inner clearfix row"]')
pizzaName = driver.find_elements_by_xpath('//h2[@class="salescloud-menu-title"]')
pizzaToppings = driver.find_elements_by_xpath('//div[@class="salescloud-default-variations-description"]')
pizzaMidPrice = driver.find_elements_by_xpath('//p[@class="salescloud-menu-price"]')
for i in range(len(pizzaName) - 1):
	print(pizzaName[i].text)
	print(pizzaToppings[i].text)
	print(pizzaMidPrice[i].text)

driver.close()