"""Pig Latin Generator. Takes a word and converts to pig latin"""
import sys

print("Pig Latin Converter!\n")

while True:
    print("\nType in a word to convert:\n")
    word = input("(type q to quit)")

    if word.lower() == "q":
        sys.exit()

    letter_test = word[0]
    VOWELS = "aeiou"
    if letter_test in VOWELS:
        output_word = word + 'way'
    else:
        output_word = word[1:] + word[0] + 'ay'
    print(output_word)
