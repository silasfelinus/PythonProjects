from itertools import product
combo = (1,  2)
for perm in product(combo, repeat = 2):
	print(perm)