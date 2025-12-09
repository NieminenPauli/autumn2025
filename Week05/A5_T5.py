"""A5_T5 Menu-driven program
Create a menu-driven Python program with following options:

Insert a word
Which stores user inserted word into memory.
Show current word
Prints the word from the memory
Show current word in reverse
Prints the word from the memory in reverse.
Exit
Stops the program gracefully
Unknown option
Initialize the Word with an empty string.

Example program runs

run 1 run 2 run 3 run 4
Program starting.
Options:
1 - Insert word
2 - Show current word
3 - Show current word in reverse
0 - Exit
Your choice: 1
Insert word: Banana

Options:
1 - Insert word
2 - Show current word
3 - Show current word in reverse
0 - Exit
Your choice: 2
Current word - "Banana"

Options:
1 - Insert word
2 - Show current word
3 - Show current word in reverse
0 - Exit
Your choice: 3
Word reversed - "ananaB"

Options:
1 - Insert word
2 - Show current word
3 - Show current word in reverse
0 - Exit
Your choice: 0
Exiting program.

Program ending.
"""
def main():
    print("Program starting.")

    Word = ""   # memory for the current word

    while True:
        print("Options:")
        print("1 - Insert word")
        print("2 - Show current word")
        print("3 - Show current word in reverse")
        print("0 - Exit")
        choice = input("Your choice: ")

        if choice == "1":
            Word = input("Insert word: ")
            print()

        elif choice == "2":
            print(f'Current word - "{Word}"')
            print()

        elif choice == "3":
            print(f'Word reversed - "{Word[::-1]}"')
            print()

        elif choice == "0":
            print("Exiting program.")
            break

        else:
            print("Unknown option.")
            print()

    print("\nProgram ending.")


if __name__ == "__main__":
    main()