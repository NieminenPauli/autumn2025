# luetaan kansio 
"""file = open("Week06/A6_T1_D1.txt","r")
while True:
    line = file.readline()
    if len(line) == 0:
        break
    print(line,end="")
file.close()"""

def openFile(name):

    file = open(f"Week06/{name}","r")
    print(f"#### START {name} ####")
    while True:
        line = file.readline()
        if len(line) == 0:
            break
        print(line, end="")
    file.close()
    print(f"#### END {name}####")
    return None

def main():
    print("Program starting")
    fileName = input("Insert filename: ")
    openFile(fileName)
    print("Program ending")

    return None
if __name__ == "__main__":
    main()