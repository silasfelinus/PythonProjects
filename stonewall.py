"""Find a six letter word that can be spelled with a specific set"""
import load_dictionary
word_list = load_dictionary.load('allwords.txt')

possible_words = []

SET1 = "srej"
SET2 = "opal"
SET3 = "tnkf"
SET4 = "dwib"
SET5 = "vuhc"
SET6 = "gxmy"

counter = 0

for letter1 in SET1:
	for letter2 in SET2:
		for letter3 in SET3:
			for letter4 in SET4:
				for letter5 in SET5:
					for letter6 in SET6:
						working_word = letter1 + letter2 + letter3 + letter4 + letter5 + letter6
						possible_words.append(working_word)
print(possible_words)

for word in possible_words:
	if word in word_list:
		print("Success")
		print(word)
