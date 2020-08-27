from users import User

class Admin(User):
	#User with elevated access
	def __init__(self, first_name, last_name):
		super().__init__(first_name, last_name)
		self.privileges = Privileges()

class Privileges():
	#privileges of users

	def __init__(self, privileges=[]):
		self.privileges = privileges

	def show_privileges(self):
		#stolen from answer page
		#otherwise would have done
		#print(self.privileges)
 		print("\nPrivileges:")
 		if self.privileges:
 			for privilege in self.privileges:
 				print("- " + privilege)
 			else:
 				print("- This user has no privileges.")


