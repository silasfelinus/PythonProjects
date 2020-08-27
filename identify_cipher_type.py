"""Determine whether a cipher is likely to be either substitution or transposition"""
import sys
from collections import Counter

# set arbitrary cutoff
CUTOFF = 2.5

# load ciphertext
def load (filename):
	""" Open text file and return list """
	with open(filename) as f:
		return f.read().strip()

try:
	ciphertext = load('a_cipher.txt')
except IOError as e:
	print("{}. Terminating program.".format(e),
			file=sys.stderr)
	sys.exit(1)

# Count 6 most common letters in ciphertext
six_most_frequent = Counter(ciphertext.lower()).most_common(6)
print("\nSix most common letters in English = ETAOIN")
print('\nSix most frequent letters in ciphertext = ')
print(*six_most_frequent, sep='\n')

# convert list of tuples to set of letters for comparison
cipher_top_6 = {i[0] for i in six_most_frequent}

TARGET = 'etaoin'
count = 0
for letter in TARGET:
	if letter in cipher_top_6:
		count += 1

if count/len(TARGET) >= CUTOFF:
	print("\nThis ciphertext most-likely produced by a TRANSPOSITION cipher")
else:
	print("\nThis ciphertext most-likely produced by a SUBSTITUTION cipher")