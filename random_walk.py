from random import choice

class RandomWalk:
	"""A class to generate random walks"""

	def __init__(self, num_points=5000):
		"""Initialize attributes for a walk."""
		self.num_points = num_points

		#all walks start at (0, 0)
		self.x_values = [0]
		self.y_values = [0]

	def get_step(self):
		direction = choice([-1, 1])
		distance = choice(range(0,8))
		return direction * distance

	def fill_walk(self):
		"""Calculate all the points on the walk"""
		while len(self.x_values) < self.num_points:

			#Decide which direction to go and how far to go in that direction
			x_direction = choice([1, -1])
			x_distance = choice(range(0, 8))
			x_step = self.get_step()

			y_direction = choice([1, -1])
			y_distance = choice(range(0, 8))
			y_step = self.get_step()

			#Reject moves that go nowhere
			if x_step == 0 and y_step == 0:
				continue

			#Calculate the new position
			x = self.x_values[-1] + x_step
			y = self.y_values[-1] + y_step

			self.x_values.append(x)
			self.y_values.append(y)