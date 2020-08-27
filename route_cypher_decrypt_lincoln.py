ciphertext = "THIS OFF DETAINED ASCERTAIN WAYLAND CORRESPONDENTS OF AT WHY AND IF FILLS IT YOU GET THEY NEPTUNE THE TRIBUNE PLEASE ARE THEM CAN UP"

# split elements into words, not letters

cipherlist = list(ciphertext.split())

# initialize variables
COLS = 4
ROWS = 6
key = '-1 2 -3 4' # neg number means read UP columns vs. DOWN
translation_matrix = [None] * COLS
plaintext = ''
start = 0
stop = ROWS

# turn key_int into list of integers:
key_int = [int(i) for i in key.split()]

# turn columns into items in list of lists
for k in key_int:
	if k < 0: # reading bottom to top
		col_items = cipherlist[start:stop]
	elif k > 0 : # reading top to bottom
		col_items = list((reversed(cipherlist[start:stop])))
	translation_matrix[abs(k) - 1] = col_items
	start += ROWS
	stop += ROWS

print("\nciphertext = {}".format(ciphertext))
print("\translation matrix =", *translation_matrix, sep = "\n")
print("\nkey length = {}".format(len(key_int)))

# loop through nested lists popping off last item to new list
for i in range(ROWS):
	for col_items in translation_matrix:
		word = str(col_items.pop())
		plaintext += word + ' '

print("\nplaintext = {}".format(plaintext))
