import requests
import json
response = requests.get("https://api.dominos.is/api/menu")

pizzas = response.json()
topping = ""
for pizza in pizzas['menu']['menuPizzas']:
	pizzaName = pizza['name']
	for i, top in enumerate(pizza['toppings']):
		if i == 0:
			topping += top['name']
		else:
			topping += ", " + top['name']
	pizzaTopping = topping
	listPizzaTopping = pizzaTopping.split(", ")
	pizzaSmallPrice = pizza['sizes'][0]['pickupPrice']
	pizzaMidPrice = pizza['sizes'][1]['pickupPrice']
	pizzaBigPrice = pizza['sizes'][2]['pickupPrice']

	topping = ""

	print("Nafn : " + pizzaName )
	print("alegg : " + pizzaTopping)
	print(listPizzaTopping)
	print(pizzaSmallPrice)
	print(pizzaMidPrice)
	print(pizzaBigPrice)	

