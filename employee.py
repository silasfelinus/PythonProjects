class Employee():
	"""blueprint for an employee that considers name and salary"""

	def __init__(self, first_name, last_name, salary):
		"""Take in name and salary"""
		self.first_name = first_name.title()
		self.last_name = last_name.title()
		self.salary = salary

	def give_raise(self, salary_increase=5000):
		self.salary += salary_increase
		print("Employee's salary is now $" + str(self.salary)) 

new_employee = Employee('Silas', 'Knight', 50000)
new_employee.give_raise()
new_employee.give_raise(1)
