responses = {}

polling_active = True

while polling_active:
		name = input ("\nWhat is your name? ")
		response = input("Where is your dream vacation? ")
		responses[name] = response

		repeat = input("Would you like to let another person respond? (yes/no) ")
		if repeat == 'no':
			polling_active = False

#Polling done, print results
print("\n--- Poll results ---")
for name, response in responses.items():
	print(name + " would like to visit " + response + ".")

end = input("Press Enter to end: ")