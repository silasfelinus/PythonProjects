import load_dictionary

word_list = load_dictionary.load('allwords.txt')

anagram_list = []

# input a single word or single name below to find its anagrams
name = 'silas'
print("Input name = {}".format(name))
name = name.lower()
print("Using name = {}".format(name))

#Sort name and find anagrams
name_sorted = sorted(name)
for word in word_list:
	word = word.lower()
	if word != name:
		if sorted(word) == name_sorted:
			anagram_list.append(word)

# print out list of anagrams
print()
if len(anagram_list) == 0:
	print("You need a larger dictionary or a new name!")
else:
	print("Anagrams = ", anagram_list, sep = '\n')