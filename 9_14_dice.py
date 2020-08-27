from random import randint

class Dice():
	""""A simple Class to represent a dice of various sides"""
	def __init__(self, sides = 6):
		self.sides = sides

	def roll_dice(self, iterations = 1):
		while iterations > 0:
			print(randint(1, self.sides))
			iterations -= 1


d6 = Dice()
d10 = Dice(10)
d20 = Dice(20)

d6.roll_dice(10)

d10.roll_dice(10)

d20.roll_dice(10)