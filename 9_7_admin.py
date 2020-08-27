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

class Admin(User):
	def __init__(self, first_name, last_name):
		super().__init__(first_name, last_name)
		self.privileges = ["can delete posts", "can see home addresses", "can access webcams remotely"]

	def show_privileges(self):
		print(self.privileges)



ronin = Admin('ronin', 'knight')

ronin.describe_user()
ronin.greet_user()

ronin.show_privileges()