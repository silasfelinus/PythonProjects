import re
from collections import defaultdict
from itertools import permutations
import load_dictionary

word_list = load_dictionary.load("allwords.txt")


test_word = "volvo"
digrams = []
for current_letter in test_word:
	test_word = test_word[1:]
	for remaining_letter in test_word:
		digrams.append(current_letter + remaining_letter)
digram_set = set(digrams)
print(digram_set)

mapped = defaultdict(int)
for word in word_list:
	word = word.lower()
	for digram in digrams:
		for m in re.finditer(digram, word):
			mapped[digram] += 1

print("Digram frequency count:")
count = 0
for k in mapped:
	print("{} {}".format(k, mapped[k]))
