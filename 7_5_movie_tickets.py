age = input("\nPlease enter your age: ")

age_int = int(age)

if age_int < 3:
	print("Your ticket will be free!")
elif age_int < 13:
	print("Your ticket will be $10.")
else:
	print("Your ticket will be $15.")

end = input("Input anything to quit: ")