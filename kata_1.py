class Number:
	"""A number being tested from the set"""

	def __init__(self, position, value, evens_seen, odds_seen):
		self.position = position
		self.value = value
		self.evens_seen = evens_seen
		self.odds_seen = odds_seen

		#check for evenness
		if int(value) % 2 == 0:
			evenness = True
			evens_seen += 1
			if evens_seen == odds_seen + 2:
				winner = True 
				even_wins = True
		else:
			evenness = False
			odds_seen += 1
			if odds_scene == evens_seen + 2:
				winner = True
				even_wins = False





def iq_test(numbers):

	"""initialize variables"""
	evens_seen = 0
	odds_seen = 0
	iteration = 0
	winner = False
	new_collection = []

	for number_tested in numbers:
		iteration +=1
		latest_number = Number(iteration, number_tested, evens_seen, odds_seen)
		new_collection.append(number_tested)

		#Do we have a winner?
		if winner == True & even_wins == True:
			for possible_outlier in new_collection:
				if possible_outlier.evenness == False:
					return possible_outlier.position

		if winner == True & even_wins == False:
			for possible_outlier in new_collection:
				if possible_outlier.evenness == True:
					return possible_outlier.position