filename = 'guestbook.txt'
quit = False
while quit == False:
	guest = input('Please sign our guestbook: ')
	if guest == 'quit':
		quit = True
	else:
		print("Hello " + guest.title() + " Thanks for visiting!\n")
		with open(filename, 'a') as file_object:
			file_object.write(guest + "\n")