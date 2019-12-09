import requests
import json
response = requests.get("https://api.pizzan.is/api/v1/pizzas/menu/")


pizzas = response.json()

for pizza in pizzas:

	pizzaName = pizza['name']
	pizzaTopping = pizza['toppingsSummary']
	listPizzaTopping = pizzaTopping.split(", ")
	pizzaSmallPrice = pizza['minimumAmountSmall']
	pizzaMidPrice = pizza['minimumAmountMedium']
	pizzaBigPrice = pizza['minimumAmountLarge']


	print("Nafn : " + pizzaName )
	print("alegg : " + pizzaTopping)
	print(listPizzaTopping)
	print(pizzaSmallPrice)
	print(pizzaMidPrice)
	print(pizzaBigPrice)	