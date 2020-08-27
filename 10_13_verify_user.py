import json

def get_stored_username():
	"""Get stored name if available"""
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username():
	"""Prompt for new username"""
	username = input("What is your name? ")
	filename = 'username.json'
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
	return username

def greet_user():
		"""Greet user by name"""
		username = get_stored_username()
		if username:
			check_user = input("Is this " + username + " (y or n)?")
			if check_user == "y"
				print("Welcome back, " +username + "!")
			else:
				username = get_new_username()
				print("We'll remember you next time, " + username + "!")
		else:
			username = get_new_username()
			print("We'll remember you next time, " + username + "!")

greet_user()
input("End?")