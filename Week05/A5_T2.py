"""A5_T2 Pass argument
Create Python program which is able to print user input with a decorative frame.

Program must consist of two functions:

main-function
Print starting and ending statements.
Print any empty row (see example program run)
Prompt user to insert a word.
Pass the inserted word into the frameWord-function.
Returns None
frameWord
Takes PWord as a parameter.
Prints the framing and the PWord
Hint: Multiply the asterisk '*'-character.
Returns None
Note! Tests for this task relies on properly defined functions and may fail if the program is not written according to the instructions.

Example program runs

run 1 run 2 run 3
Program starting.
Insert word: Beautiful

*************
* Beautiful *
*************

Program ending.
"""
def framework(PWord):
    asteri = "*"
    print(asteri * len(PWord) + 2 * asteri )
    print(f"*{PWord}*")
    print(asteri * len(PWord) + 2 * asteri )
    return None


def main ():
    print("Program starting")
    word = input("Inser word: ")
    print("")
    framework(word)
    print("")

    print("Programn ending")

    return None

main()