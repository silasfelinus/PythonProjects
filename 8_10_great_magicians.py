def show_magicians(magicians):
	for magician in magicians:
		print(magician.title())

def make_great(magicians):
	great_magicians = []
	while magicians:
		magician = magicians.pop()
		great_magician = magician + " The Great"
		great_magicians.append(great_magician)
	for great_magician in great_magicians:
		magicians.append(great_magician)





magicians = ['copperfield', "Houdini", 'GOB Bluth']
show_magicians(magicians)

make_great(magicians)

show_magicians(magicians)