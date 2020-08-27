class User():
	"""A basic user to explore Classes"""

	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.full_name = self.first_name.title() + " " + self.last_name.title()
		self.login_attempts = 0

	def describe_user(self):
		print("User's name is " + self.full_name)

	def greet_user(self):
		print("Hello, " + self.full_name + "!")

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0


fox = User('fox', 'knight')

fox.describe_user()
fox.greet_user()

fox.increment_login_attempts()
fox.increment_login_attempts()
fox.increment_login_attempts()

print(fox.login_attempts)

fox.reset_login_attempts()

print(fox.login_attempts)