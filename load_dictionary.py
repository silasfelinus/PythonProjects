"""Loads a text file as a list

Arguments:
-Text file name (and directory, if needed)

Exceptions:
-IOError if filename not found

Returns:
A list of all words in a text file in lower case

"""
import sys

def load(file):
	"""Open a text file and return a list of lowercase strings"""
	try:
		with open(file) as in_file:
			loaded_txt = in_file.read().split('\n')
			loaded_txt = [x.lower() for x in loaded_txt]
			return loaded_txt
	except IOError as e:
		print("{}\nError opening {}. Terminating program.".format(e, file),
			file = sys.stderr)
		sys.exit(1)