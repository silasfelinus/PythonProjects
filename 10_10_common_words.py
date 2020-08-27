def file_error(filename):
	"""error to print if file is not found"""
	msg = "Sorry, the file " + filename + " can't be found."
	print(msg)

def count_word(book, word):
	"""count the number of times a particular word appears in a book"""
	try:
		with open(book) as f_obj:
			book_text = f_obj.read()
			word_count = book_text.lower().count(word)
			print("\nThe word '" + word + "' appears " + str(word_count) + " times in " + book)

	except FileNotFoundError:
		file_error(book)


books = ['mermaids.txt', 'bible.txt', 'alice.txt']
word = "beasts"

for book in books:
	count_word(book, word)



