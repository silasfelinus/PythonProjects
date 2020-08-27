import unittest
from city_functions import make_city_country

class MakeCityCountryTestCase(unittest.TestCase):
	"""Tests city country"""

	def test_make_city_country(self):
		"""do Santiago, Chile work?"""
		test_location = make_city_country('santiago', 'chile')
		self.assertEqual(test_location, 'Santiago, Chile')

	def test_make_city_country_population(self):
		"""do Santiago, Chile work when including population??"""
		test_location = make_city_country('santiago', 'chile', population = 5000000)
		self.assertEqual(test_location, 'Santiago, Chile Population=5000000')

unittest.main()