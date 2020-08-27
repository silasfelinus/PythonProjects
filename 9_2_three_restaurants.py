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
his_restaurant = Restaurant('burger king', 'sushi')
her_restaurant = Restaurant("tomos", 'tex-mex')

my_restaurant.describe_restaurant()
his_restaurant.describe_restaurant()
her_restaurant.describe_restaurant()
