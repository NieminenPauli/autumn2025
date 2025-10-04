"""A3_T4 More menu options
Extend the previous menu program by adding three more options to the menu.

Options:

Print the name backwards
Your name backwards is "{NameBackwards}"
Print the first character
The first character in name "{Name}" is "{FirstChar}"
Show the amount of characters in the name
There are {NameLength} characters in the name "{Name}"
run 1 run 2 run 3 run 4 run 5 run 6
Program starting.
This is a program with simple menu, where you can choose which operation the program performs.
Before the menu, please insert your name: John

Options:
1 - Print welcome message
2 - Print the name backwards
3 - Print the first character
4 - Show the amount of characters in the name
0 - Exit
Your choice: 1
Welcome John!

Program ending.
"""
print("Programn starting")
name =input("This is a program with simple menu, where you can choose which operation the program performs.\nBefore the menu, please insert your name: ")

print("Options")
print("1 - Print welcome message")
print("2 - Print the name backwards")
print("3 - Print the first character")
print("4 - Show the amount of characters in the name")
print("0 - Exit")

choice = int(input("Your choice: "))

if choice == 1:
    print(f"Welcome {name}!")
elif choice == 2:
    print(name[::-1])
elif choice == 3:
    print(choice[0])
elif choice == 4:
    print(len(name))
elif choice == 0:
    print("Program ending")    