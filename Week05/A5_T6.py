def showOptions() -> None:
    print("Options:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")


def askChoice() -> int:
    choice = input("Your choice: ")

    if not choice.isnumeric():
        print("Unknown option!")
        print()
        return -1

    return int(choice)


def main() -> None:
    print("Program starting.")

    count = 0

    while True:
        showOptions()
        choice = askChoice()

        if choice == 1:
            print(f"Current count - {count}")
            print()

        elif choice == 2:
            count += 1
            print("Count increased!")
            print()

        elif choice == 3:
            count = 0
            print("Cleared count!")
            print()

        elif choice == 0:
            print("Exiting program.")
            break

        elif choice != -1: 
            print("Unknown option!")
            print()

    print()
    print("Program ending.")



main()