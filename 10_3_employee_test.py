import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
	'''Tests the employee class'''

	def setUp(self):
		'''create a sample employee for testing purposes'''
		self.new_employee = Employee('silas', 'knight', 50000)

	def  test_give_default_raise(self):
		'''test default raise'''
		self.new_employee.give_raise()
		self.assertEqual(self.new_employee.salary, 55000)



	def test_give_custom_raise(self):
		'''test custom raise'''
		self.new_employee.give_raise(5)
		self.assertEqual(self.new_employee.salary, 50005)

unittest.main()