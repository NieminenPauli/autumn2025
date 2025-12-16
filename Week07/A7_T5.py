DELIMITER = ";"

WEEKDAYS = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturnday", 
    "Sunday",
)


class TIMESTAMP:
    def __init__(self):
        self.weekday = ""
        self.hour = ""
        self.consumption = 0.0
        self.price = 0.0


def readTimestamps(filename: str, timestamps: list[TIMESTAMP]) -> None:
  
    print(f'Reading file "{filename}".')

    timestamps.clear()

    with open(filename, "r", encoding="utf-8") as f:
        header = f.readline() 

        for line in f:
            row = line.rstrip()
            if row == "":
                continue  

            columns = row.split(DELIMITER)
        

            ts = TIMESTAMP()
            ts.weekday = columns[0]
            ts.hour = columns[1]
            ts.consumption = float(columns[2])
            ts.price = float(columns[3])

            timestamps.append(ts)

    return None


def analyseTimestamps(timestamps: list[TIMESTAMP], results: list[str]) -> None:
 
    print("Analysing timestamps.")

   
    daily_usage: list[float] = [0.0] * 7
    daily_cost: list[float] = [0.0] * 7

   
    for ts in timestamps:
        
        for i, wd in enumerate(WEEKDAYS):
            if ts.weekday == wd:
                daily_usage[i] += ts.consumption
                daily_cost[i] += ts.consumption * ts.price
                break

    
    results.clear()
    results.append("### Electricity consumption summary ###")

    for i, wd in enumerate(WEEKDAYS):
        usage = daily_usage[i]
        cost = daily_cost[i]
        results.append(
            f" - {wd} usage {usage:.2f} kWh, cost {cost:.2f} €"
        )

    results.append("### Electricity consumption summary ###")

    return None


def displayResults(results: list[str]) -> None:
    print("Displaying results.")
    for line in results:
        print(line)
    return None


def main() -> None:
    print("Program starting.")

    filename = input("Insert filename: ")
    timestamps: list[TIMESTAMP] = []
    results: list[str] = []

    readTimestamps(filename, timestamps)
    analyseTimestamps(timestamps, results)
    displayResults(results)

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
