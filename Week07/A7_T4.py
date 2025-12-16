DELIMITER = ";"

class TIMESTAMP:
    def __init__(self):
        self.weekday = ""
        self.hour = ""          # pidetään stringinä (esim. "00:00")
        self.consumption = 0.0  # HUOM: kirjoitusasu korjattu
        self.price = 0.0

def readfile():
    file = input("Insert filename: ")
    print(f'Reading file "{file}".')
    TimeStampList = []

    with open(file, "r", encoding="utf-8") as f:
        header = f.readline()

        for line in f:
            row = line.rstrip()

            if row == "":           # ohitetaan tyhjät rivit
                continue

            columns = row.split(DELIMITER)
            TimeStamp = TIMESTAMP()
            TimeStamp.weekday = columns[0]
            TimeStamp.hour = columns[1]
            TimeStamp.consumption = float(columns[2])  # string -> float
            TimeStamp.price = float(columns[3])

            TimeStampList.append(TimeStamp)

    analyzedata(TimeStampList)
    return None


def analyzedata(TimeStampList):
    print("Electricity usage:")

    totalConsumption = 0.0
    totalCost = 0.0

    for ts in TimeStampList:
        rowCost = ts.consumption * ts.price
        totalConsumption += ts.consumption
        totalCost += rowCost

        print(
            f" - {ts.weekday} {ts.hour}, "
            f"price {ts.price:.2f}, "
            f"consumption {ts.consumption:.2f} kWh, "
            f"total {rowCost:.2f} €"
        )

   

    return None

def main():
    print("Program starting.")
    readfile()
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()
