"""A2_T5 String length and slicing (TEST TASK)
Make a Python program, which prompts for a compound word.

Get following aspects from the word
Length
First character
Reversed version e.g. “Suitcase” is reversed “esactiuS”
Display the aspects using print commands.
Prompt the user to take substring from the existing compound word.
Finally print the user specified substring.
Example program run:

Program starting.

Insert a closed compound word: Moonbanana
The word you inserted is 'Moonbanana' and in reverse it is 'ananabnooM'.
The inserted word length is 10
Last character is 'a'

Take substring from the inserted word by inserting...
1) Starting point: 0
2) Ending point: 4
3) Step size: 1

The word 'Moonbanana' sliced to the defined substring is 'Moon'.
Program ending."""

print("Programn starting")
compoundWord = input("Insert a closed compound word: ")
reversedCompoundWord = compoundWord[::-1]
print(f"The word you inserted is '{compoundWord}' and reverse it is {reversedCompoundWord}")
print(f"The inserted word legnht is {len(compoundWord)}")
print(f"The last character is {compoundWord[-1]}")

print("Take substring from the inserted word by inserting...")

startingPoint = int(input("Starting point: "))
endingPoint = int(input("Ending point: "))
stepSize = int(input("Step size: "))

subString = compoundWord[startingPoint:endingPoint:stepSize]

print(f"The word '{compoundWord}' sliced to the defined substring is '{subString}'.")
print("Programn ending")


