"""Load a dict file, pick random words, run syllable-counting module"""
import sys
import random
from test_count import count_syllables

def load(file):
	"""Open a text file & return list of lowercase strings"""
	with open(file) as in_file:
		loaded_txt = in_file.read().strip().split('\n')
		loaded_txt = [x.lower() for x in loaded_txt]
		return loaded_txt
try:
	word_list = load('allwords.txt')
except IOError as e:
	print("{}\nError opening file. Terminating program.".format(e), file=sys.stderr)
	sys.exit(1)

test_data = []
num_words = 200
test_data.extend(random.sample(word_list, num_words))
print(test_data)

for word in test_data:
	try:
		num_syllables = count_syllables(word)
		print(word, num_syllables, end='\n')
	except KeyError:
		print(word, end=' ')
		print(" not found", file=sys.stderr)