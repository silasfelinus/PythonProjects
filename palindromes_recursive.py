"""Find palindromes ina dictionary file"""
import load_dictionary


def test_word(word):
	stripped_word = word
	while len(stripped_word) > 1:
		if stripped_word[0] == stripped_word[-1]:
			stripped_word = stripped_word[1:-1]
		else:
			return False
	return True


word_list = load_dictionary.load('allwords.txt')
permissible = ('a', 'i')
for word in word_list:
	if len(word) == 1 and word not in permissible:
		word_list.remove(word)

pali_list = []
words = set(word_list)
for word in words:
	if test_word(word):
		pali_list.append(word)

print("\nNumber of palindromes found = {}\n".format(len(pali_list)))
print(*pali_list, sep='\n')