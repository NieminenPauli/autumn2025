def showOptions() -> None:
   
    print("Options:")
    print("1 - Insert line")
    print("2 - Save lines")
    print("0 - Exit")


def askChoice() -> int:
   
    try:
        return int(input("Your choice: "))
    except ValueError:
       
        return -1


def saveLines(PLines: list[str]) -> None:
    
    if not PLines:
       
        return

    try:
        filename = input("Insert filename: ")
        with open(filename, "w", encoding="UTF-8") as f:
          
            f.writelines(PLines)
    except Exception as e:
        print(f"Error saving file: {e}")


def insertLine(PLines: list[str]) -> None:
   
    text = input("Insert text: ")
    PLines.append(text)


def onInterrupt(PLines: list[str]) -> None:
   
    if not PLines:
        # no unsaved data
        print("Closing suddenly.")
        return

    print("Keyboard interrupt and unsaved progress!")
    try:
        answer = input("Save before quit(y/n)?: ").strip().lower()
    except Exception:
      
        return

    if answer == "y":
        saveLines(PLines)
   


def main() -> None:
    Lines: list[str] = []
    Choice = -1
    print("Program starting.")

    try:
        while Choice != 0:
            showOptions()
            Choice = askChoice()
            if Choice == 1:
                insertLine(Lines)
            elif Choice == 2:
                saveLines(Lines)
            elif Choice == 0:
                print("Exiting program.")
            else:
                print("Unknown option!")
            print("")
    except KeyboardInterrupt:
        # Handle CTRL + C
        if Lines:
            onInterrupt(Lines)
        else:
            print("Closing suddenly.")

    Lines.clear()
    print("Program ending.")


if __name__ == "__main__":
    main()
