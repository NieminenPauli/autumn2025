WEEKDAYS: tuple[str, ...] = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturnday",
    "Sunday",
)


def readFile(PFilename: str, PRows: list[str]) -> None:
    print('Reading file "{}".'.format(PFilename))

    
    PRows.clear()

   
    with open(PFilename, "r", encoding="utf-8") as file:
        

        
        header = file.readline()

       
        for line in file:
            
            line = line.strip()

          
            if line == "":
                continue

            
            PRows.append(line)

   
    return None


def analyseTimestamps(PRows: list[str], PResults: list[str]) -> None:
    print("Analysing timestamps.")

    
    PResults.clear()

   
    WeekdayTimestampAmount: list[int] = [0, 0, 0, 0, 0, 0, 0]

   
    for row in PRows:
      
        for j, weekday in enumerate(WEEKDAYS):
            
            if row.startswith(weekday):
                WeekdayTimestampAmount[j] += 1
                break  

  
    for i, weekday in enumerate(WEEKDAYS):
        count = WeekdayTimestampAmount[i]
        PResults.append(f" - {weekday} {count} stamps")

    
    WeekdayTimestampAmount.clear()

    return None


def displayResults(PResults: list[str]) -> None:
    print("Displaying results.")
    print("### Timestamp analysis ###")
    for line in PResults:
        print(line)
    print("### Timestamp analysis ###")
    return None


def main() -> None:
    print("Program starting.")

    # 1. Initialise
    rows: list[str] = []
    results: list[str] = []

    # 2. Operate
    filename = input("Insert filename: ")

    # 2.2. Read file
    readFile(filename, rows)

    # 2.3. Analyse rows
    analyseTimestamps(rows, results)

    # 2.4. Display results
    displayResults(results)

    # 3. Cleanup
    rows.clear()
    results.clear()

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()


