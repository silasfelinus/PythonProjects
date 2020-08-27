def dig_pow(n, p):
	total = 0
	numbers = [int(d) for d in str(n)]
	for number in numbers:
		total += number**p
		p += 1

	increment = 1

	while (n * increment) <= total:
		if n * increment == total:
			print(increment)
			return increment
		else:
			increment += 1
	return -1





dig_pow(89, 1)
dig_pow(92, 1)
dig_pow(46288, 3)
