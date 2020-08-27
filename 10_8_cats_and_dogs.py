def file_error(filename):
	msg = "Sorry, the file " + filename + " can't be found."
	print(msg)

cat_file = "cats.txt"
dog_file = "dogs.txt"

try:
	with open(cat_file) as f_obj:
		cat_names = f_obj.read()
		cats = cat_names.split()
		print("Cat names are: ")
		print(cats)

except FileNotFoundError:
	file_error(cat_file)

try:
	with open(dog_file) as f_obj:
		dog_names = f_obj.read()
		dogs = dog_names.split()
		print("Dog names are: ")
		print(dogs)

except FileNotFoundError:
	file_error(dog_file)

