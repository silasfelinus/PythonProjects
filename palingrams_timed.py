"""Find all word-pair palingrams in a dictionary file"""
import load_dictionary
import time



word_list = load_dictionary.load('words.txt')
permissible = ('a', 'i')
for word in word_list:
	if len(word) == 1 and word not in permissible:
		print(word)
		word_list.remove(word)

#Find word pair palingrams
def find_palingrams():
	"""Find dictionary palingrams"""
	pali_list = []
	words = set(word_list)
	for word in words:
		end = len(word)
		rev_word = word[::-1]
		if end > 1:
			for i in range(end):
				if word[i:] == rev_word[:end - i] and rev_word[end - i:] in words:
					pali_list.append((word, rev_word[end - i:]))
				if word[:i] == rev_word[end - i:] and rev_word[:end - i] in words:
					pali_list.append((rev_word[:end - i], word))
	return pali_list

#timer
start_time = time.time()

palingrams = find_palingrams()

#timer
end_time = time.time()

#Sort palingrams on first word
palingrams_sorted = sorted(palingrams)

#Display list of palingrams
print("\nNumber of palingrams = {}\n".format(len(palingrams_sorted)))
for first, second in palingrams_sorted:
	print("{} {}".format(first, second))



print("Runtime for this program was {} seconds.".format(end_time - start_time))
