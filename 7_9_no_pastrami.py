sandwich_orders = ['pastrami', 'BLT', 'pastrami', 'pastrami', 'cheese']
finished_sandwiches = []

if 'pastrami' in sandwich_orders:
	print("Oh no, we're out of pastrami!")
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

while sandwich_orders:
	order = sandwich_orders.pop()
	print("\nI'm making your " + order + " sandwich." )
	finished_sandwiches.append(order)
print("I'm done!")
print(finished_sandwiches)