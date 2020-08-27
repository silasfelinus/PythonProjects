class Restaurant():
	"""A basic restaurant to explore Classes"""

	def __init__(self, name, cuisine):
		self.name = name
		self.cuisine = cuisine

	def describe_restaurant(self):
		print(self.name.title() + ": " + self.cuisine)



	def open_restaurant(self):
		print(self.name.title() + " is open!")

my_restaurant = Restaurant('mcdonalds', "fine dining")

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
