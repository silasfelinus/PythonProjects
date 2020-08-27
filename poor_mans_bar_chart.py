"""Poor Man's Pie Chart
Take in a string and output 
the number of times each letter appears"""
import pprint
import sys
from collections import defaultdict

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
print("Poor Man's Pie Chart")
while True:
	phrase = input("Please input a short phrase:")
	if phrase == 'q':
		sys.exit()

	abc_counter = defaultdict(list)
	for character in phrase:
		character = character.lower()
		if character in ALPHABET:
			abc_counter[character].append(character)

	print("text = ", end = '')
	print("{}\n".format(phrase), file = sys.stderr)
	pprint.pprint(abc_counter, width = 110)