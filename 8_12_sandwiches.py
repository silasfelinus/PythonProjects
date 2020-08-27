def sandwich_order (*fillings):
	print("\nMaking a sandwich with the following item(s): ")
	for filling in fillings:
		print(filling)

sandwich_order('blt')
sandwich_order('bacon', 'lettuce', 'guac')
sandwich_order('salami','cheese')

