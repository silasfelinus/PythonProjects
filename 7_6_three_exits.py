prompt = "\nPlease enter a topping"
prompt += "\nInput 'quit' to end: "

topping = input(prompt)

while topping != 'quit':
	print("We'll add " + topping + " to your order!")
	topping = input(prompt)
	continue
