class Restaurant():
	"""A basic restaurant to explore Classes"""

	def __init__(self, name, cuisine):
		self.name = name
		self.cuisine = cuisine
		self.number_served = 0

	def describe_restaurant(self):
		print(self.name.title() + ": " + self.cuisine)

	def set_number_served(self, number):
		self.number_served = number

	def increment_number_served(self, increment):
		self.number_served += increment


	def open_restaurant(self):
		print(self.name.title() + " is open!")

class IceCreamStand(Restaurant):
	#a restaurant that sells ice cream

	def __init__(self, name, cuisine = "ice cream"):
		super().__init__(name, cuisine)
		self.flavors = []

	def display_favors(self):
		print(self.flavors)

