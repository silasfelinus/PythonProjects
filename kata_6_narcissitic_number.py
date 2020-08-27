def narcissistic( value ):
	"""take a number and return true or false if it is narcissistic"""
	exponent = len(str(value))
	numbers = [int(d) for d in str(value)]
	total = 0
	for number in numbers:
		total += number**exponent
	return total == value

print(narcissistic(7))
print(narcissistic(371))
print(narcissistic(122))
print(narcissistic(4887))
