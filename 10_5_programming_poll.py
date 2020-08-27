filename = 'program_poll.txt'
quit = False
while quit == False:
	poll = input('Why do you like programming?: ')
	if poll == 'quit':
		quit = True
	else:
		with open(filename, 'a') as file_object:
			file_object.write(poll + "\n")