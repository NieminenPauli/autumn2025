SEPARATOR = ";"

def readValues(fileName: str) -> list[int]:
    numbers = []

    with open(fileName, "r") as file:
        for line in file:
            line = line.strip()
            if line.isdigit():      # varmistaa että rivillä on numero
                numbers.append(int(line))

    return numbers


def analyseNumbers(numbers: list[int]) -> tuple[int, int, int, float]:
    count = len(numbers)
    total = sum(numbers)
    greatest = max(numbers)
    average = total / count
    return count, total, greatest, average


def displayResults(fileName: str, count: int, total: int, greatest: int, average: float):
    print("#### Number analysis - START ####")
    print(f'File "{fileName}" results:')
    print("Count;Sum;Greatest;Average")
    print(f"{count}{SEPARATOR}{total}{SEPARATOR}{greatest}{SEPARATOR}{average:.2f}")
    print("\n#### Number analysis - END ####")


def main():
    print("Program starting.")
    fileName = input("Insert filename: ")

    numbers = readValues(fileName)
    count, total, greatest, average = analyseNumbers(numbers)
    displayResults(fileName, count, total, greatest, average)

    print("Program ending.")


main()