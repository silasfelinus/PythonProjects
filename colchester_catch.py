""" solve a null cipher based on every nth letter in every nth word"""
import sys

loaded_message = """Sir John:  Odd and too hard, your lot.  Still, we will band together and, like you, persevere. 
Who else could love their enemies, stand firm when all others fail, hate and despair? 
While we all can, let us feel hope. -R.T."""

# check message and # of lines
print("\nORIGINAL MESSAGE = {}\n".format(loaded_message))

#  convert message to list and get length
message = loaded_message.split()
end = len(message)

# get user input on interval to check
increment = int(input("Input max word and letter position to check: "))
print()

# find letters at designated intervals
for i in range(1, increment + 1):
	print("\nUsing increment letter {} or word {}".format(i, i))
	print()
	count = i - 1
	location = i - 1
	for index, word in enumerate(message):
		if index == count:
			if location < len(word):
				print("letter = {}".format(word[location]))
				count += i
			else:
				print("Interval doesn't work", file = sys.stderr)

end = input("end?")