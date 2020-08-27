print("Please give me two numbers to add:")

while True:
	try:
		first_number = input("\nFirst Number: ")
		first_number = int(first_number)

		second_number = input("Second Number: ")
		second_number = int(second_number)

	except ValueError:
		print("I can't add letters!")

	else:
		answer = int(first_number) + int(second_number)
		print(answer)

input("end")