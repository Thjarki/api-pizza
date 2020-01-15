from selenium import webdriver
import time
driver = webdriver.Firefox()

driver.get('https://devitos.is/menu/')
#webdriver.support.expected_conditions.presence_of_all_elements_located(driver.find_elements_by_xpath('//p[@class="menuItemName"]'))
time.sleep(2)
pizzaName = driver.find_elements_by_xpath('//p[@class="menuItemName"]')
pizzaToppings = driver.find_elements_by_xpath('//p[@class="menuItemToppings"]')
smallBasePrice = int(driver.find_element_by_id('basePrice10').text)
medBasePrice = int(driver.find_element_by_id('basePrice12').text)
bigBasePrice = int(driver.find_element_by_id('basePrice16').text)
XLBasePrice = int(driver.find_element_by_id('basePrice18').text)

smallToppingBasePrice = int(driver.find_element_by_id('price10').text)
medToppingBasePrice = int(driver.find_element_by_id('price12').text)
bigToppingBasePrice = int(driver.find_element_by_id('price16').text)
XLToppingBasePrice = int(driver.find_element_by_id('price18').text)
print(pizzaName[0].text)
for i in range(4, len(pizzaName) - 1):
	
	pizzatoppingsList = pizzaToppings[i].text.replace(" og ",", " ).split(", ")
	if(len(pizzatoppingsList)) > 1 :
		print(pizzaName[i].text)
		print(pizzatoppingsList)
		'''for topping in pizzatoppingsList:
			if topping == 'Ostur' or topping == 'Devitos sósa':
				pizzatoppingsList.remove(topping)'''
		pizzatoppingsList = [topping for topping in pizzatoppingsList if topping != 'Ostur' and topping != 'Devitos sósa']

		pizzaSmallPrice = len(pizzatoppingsList) * smallToppingBasePrice + smallBasePrice
		pizzaMedPrice = len(pizzatoppingsList) * medToppingBasePrice + medBasePrice
		pizzaBigPrice = len(pizzatoppingsList) * bigToppingBasePrice + bigBasePrice
		pizzaXLPrice = len(pizzatoppingsList) * XLToppingBasePrice + XLBasePrice
		
		print(pizzaSmallPrice)
		print(pizzaMedPrice)
		print(pizzaBigPrice)
		print(pizzaXLPrice)

driver.close()

	#print(pizzaMidPrice[i].text)