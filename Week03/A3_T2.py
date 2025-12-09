"""A3_T2 String comparisons
Make Python program which does the following steps:

Prompt user to insert
A word
A character
Find if the character exists in the word. Possible prints below.
Word "{WordFirst}" contains character "{Character}"
Word "{WordFirst}" doesn't contain character "{Character}"
Prompt user to insert one more word
Compare the first word to the second word. Examples below:
The first word "{WordFirst}" is before the second word "{WordSecond}" alphabetically.
The second word "{WordSecond}" is before the first word "{WordFirst}" alphabetically.
Both inserted words are the same alphabetically, "{WordFirst}"
Example program run

run 1 run 2 run 3
Program starting.
String comparisons
Insert first word: beans
Insert a character: n
Word "beans" contains character "n"
Insert second word: banana
The second word "banana" is before the first word "beans" alphabetically.
Program ending.
"""
print("Programn is starting")

firstWord = input("Insert a word: ")
character = input("Insert a character: ")

if character in firstWord:
    print(f"{firstWord} contains character {character}")
else:
    print(f"{firstWord} doesn't  contain character {character}")

secondWord = input("Enter second word: ")

if firstWord > secondWord :
    print(f"The first word {firstWord} is before the second word {secondWord} alphabetically")
else:
    print(f"The second word {secondWord} is before the first word {firstWord} aplhabetically")


    print("Program is ending")