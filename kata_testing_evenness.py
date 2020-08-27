#Take a list of numbers and return the position
#of the number that doesn't match 
#the evenness or oddness of the others
#Silas Knight


def even_is_normal(collection):
	print("i'm here")
	position = 0
	for number in collection:
		position += 1
		if number % 2 == 1:
			return position

def odd_is_normal(collection):
	print(collection)
	position = 0
	for number in collection:
		position += 1
		if number % 2 == 0:
			return position


def iq_test(numbers):

	"""initialize variables"""
	evens = 0
	odds = 0
	collection = [int(tester) for tester in numbers.split() if tester.isdigit()]
	print(collection)

	for number in collection:
		
		if number % 2 == 0:
			evens += 1	
		else:
			odds += 1


		if evens == odds + 2:
				return even_is_normal(collection)

		if odds == evens + 2:
				return odd_is_normal(collection)

	#If we've reached the end of the collection
	if evens > odds:

		return even_is_normal(collection)
	else:
		return odd_is_normal(collection)


print(iq_test("2 4 7 8 10"))

print(iq_test("1 2 2"))