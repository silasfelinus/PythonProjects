"""Find three letter word combos that can be spelled with a specific set"""
import load_dictionary
word_list = load_dictionary.load('allwords.txt')

possible_words = []

SET1 = "srej"
SET2 = "opal"
SET3 = "tnkf"
SET4 = "dwib"
SET5 = "vuhc"
SET6 = "gxmy"


for letter1 in SET1:
	for letter2 in SET2:
		for letter3 in SET3:
						working_word = letter1 + letter2 + letter3
						if working_word in word_list:
							possible_words.append(working_word)

print("First set: \n")
print(possible_words)

possible_words2 = []

for letter4 in SET4:
	for letter5 in SET5:
		for letter6 in SET6:
						working_word = letter4 + letter5 + letter6
						if working_word in word_list:
							possible_words2.append(working_word)

print("\nSecond set: \n")
print(possible_words2)
