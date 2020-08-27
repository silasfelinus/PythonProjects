class User():
	"""A basic user to explore Classes"""

	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.full_name = self.first_name.title() + " " + self.last_name.title()

	def describe_user(self):
		print("User's name is " + self.full_name)



	def greet_user(self):
		print("Hello, " + self.full_name + "!")

fox = User('fox', 'knight')
k8 = User('k8', 'knight')
ronin = User('ronin', 'knight')

k8.describe_user()
k8.greet_user()


fox.describe_user()
fox.greet_user()


ronin.describe_user()
ronin.greet_user()