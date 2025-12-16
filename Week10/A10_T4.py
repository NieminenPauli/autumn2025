
import sys
from A10_TLib import readValues, displayValues, mergeSort


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

    # Print raw values
    displayValues("Raw", Filename, Values)

    # Sort ascending
    AscValues = Values.copy()
    mergeSort(AscValues, PAsc=True)
    displayValues("Ascending", Filename, AscValues)

    # Sort descending
    DescValues = Values.copy()
    mergeSort(DescValues, PAsc=False)
    displayValues("Descending", Filename, DescValues)

    # Clear list (ei pakollista, mutta siisti)
    Values.clear()


if __name__ == "__main__":
    main()
