sandwich_orders = ['pastrami', 'BLT', 'cheese']
finished_sandwiches = []

while sandwich_orders:
	order = sandwich_orders.pop()
	print("I'm making your " + order + " sandwich." )
	finished_sandwiches.append(order)
print("I'm done!")
print(finished_sandwiches)