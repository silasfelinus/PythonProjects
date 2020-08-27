import json

def ask_for_favorite_number():
	"""asks for favorite number and stores in json"""
	favorite_number = input("What is your favorite number? ")
	filename = 'favorite_number.json'
	with open(filename, 'w') as f_obj:
		json.dump(favorite_number, f_obj)

def get_favorite_number():
	filename = "favorite_number.json"
	try:
		with open(filename) as f_obj:
			favorite_number = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return favorite_number


favorite_number = get_favorite_number()
if favorite_number:
	print("Your favorite number is " + favorite_number)
else:
	ask_for_favorite_number()
