"""read the contents of a file three different ways"""
filename = 'learning_python.txt'

#storing the lines and looping through the lines
with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	line = line.replace('Python', 'C')
	print(line.strip())