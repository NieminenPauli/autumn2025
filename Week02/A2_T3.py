"""A2_T3: String length and concatenation
Make Python program, which prompts user to insert two words. Print the length of each 
word and then compound them together. Put single quotes around the compound word.

Example program run:

Program starting.
Insert first word: fire
Insert second word: fighter
1st word is 4 characters long.
2nd word is 7 characters long.
Words together makes one closed compound 'firefighter'.
Program ending."""

print("Program starting")
firstWord = input("Insert first word: ")
secondWord = input("Insert second word: ")

print(f"1st word is {(len(firstWord))} charagters long")
print(f"2nd word is {(len(secondWord))} charagters long")
print(f"Words together makes one closed compound {firstWord + secondWord}")
print("Program Ending")