topping = "\nPlease enter a topping"
topping += "\nInput 'quit' to end: "

while True:
		pizza = input(topping)

		if pizza =='quit':
			break
		else:
			print("We'll add " + pizza + " to your order!")