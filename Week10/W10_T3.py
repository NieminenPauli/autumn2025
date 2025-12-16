# main.py
import sys
from Week10.A10_TLib import readValues, displayValues, bubbleSort

def main() -> None:
    # Initialize
    Values: list[int] = []
    Filename = ""

    print("Program starting.")

    # Handle CLI argument or prompt for filename
    if len(sys.argv) == 2:
        Filename = sys.argv[1]
        print(f"The filename '{Filename}' was passed via CLI.")
    else:
        Filename = input("Insert filename: ")

    # Read values from file into Values list using readValues()
    Values = readValues(Filename)

    # Print raw values using displayValues()
    displayValues("Raw", Filename, Values)

    # Sort values in ascending order using bubbleSort()
    AscValues = Values.copy()
    bubbleSort(AscValues, PAsc=True)
    # Print sorted ascending values
    displayValues("Ascending", Filename, AscValues)

    # Sort values in descending order using bubbleSort(PAsc=False)
    DescValues = Values.copy()
    bubbleSort(DescValues, PAsc=False)
    # Print sorted descending values
    displayValues("Descending", Filename, DescValues)

    # Clear list
    Values.clear()

if __name__ == "__main__":
    main()
