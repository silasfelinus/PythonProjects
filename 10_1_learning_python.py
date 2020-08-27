"""read the contents of a file three different ways"""
filename = 'learning_python.txt'

#as file object
with open(filename) as file_object:
		contents = file_object.read()
		print(contents)

print('\n')

#looping through the file
with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())

print('\n')

#storing the lines and looping through the lines
with open(filename) as file_object:
	lines = file_object.readlines()
for line in lines:
	print(line.strip())