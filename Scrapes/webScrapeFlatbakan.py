from selenium import webdriver

driver = webdriver.Firefox()

driver.get('https://www.flatbakan.is/baejarlind')

#pizzas = driver.find_elements_by_xpath('//div[@class="salescloud-product-inner clearfix row"]')
pizzas = driver.find_element_by_id('1756875695')
pizzaName = pizzas.find_elements_by_class_name('salescloud-menu-title')
pizzaToppings = pizzas.find_elements_by_class_name('salescloud-menu-description')
pizzaMidPrice = pizzas.find_elements_by_class_name('salescloud-menu-price')
print(pizzaName[0].text)
print(len(pizzaToppings))
print(len(pizzaMidPrice))
for i in range(len(pizzaName)):
	print(pizzaName[i].text)
	print(pizzaToppings[i].find_elements_by_xpath('p')[0].text)
	print(pizzaMidPrice[i].text)

driver.close()