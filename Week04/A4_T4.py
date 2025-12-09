"""A4_T4 Repetitive prompt
Make a program, which prompts user to insert words.
 Program must stop prompting words if user inserts empty word
 . After stopping the repetitive prompt, print the amount of
 words and characters that the user inserted.

Example program run:

run 1 run 2 run 3
Program starting.

Insert word (empty stops): Close
Insert word (empty stops): the
Insert word (empty stops): loop
Insert word (empty stops): 

You inserted:
- 3 words
- 12 characters

Program ending."""

print("Program starting")

words = 0
characters = 0

while True:
    word=input("Insert word (empty stops): ")

    if word == "":
        break
    words +=1
    characters+= len(word)


print("You inserted:")
print(f"{words} words")
print(f"{characters} characters")

print("\nProgram ending")