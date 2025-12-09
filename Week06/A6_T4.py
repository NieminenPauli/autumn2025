#A6_T4_D1.txt
#A6_T4_D2.txt
#A6_T4_D3.txt

#analyse names

#1 amount
# 2 shortest
#3 longest
#4 average
def DoStuff():
    fileName = input("Insert filename to read: ")
    names = []

    file = open(f"Week06/{fileName}","r")
    while True:
        line = file.readline().strip()
        
        if len(line) == 0:
            break
        names.append(line)
    print("Analysing names...")
    amount = len(names)
    shortest = min(names, key= len)
    longest = max(names, key =len)
    average = sum(len(n) for n in names) / len(names)

    file.close()
    
    print("Analysis complete")
    print("#### REPORT BEGING ####")
    print(f"Name count {amount}")
    print(f"Shortest name {len(shortest)} chars")
    print(f"Longest name {len(longest)} chars")
    print(f"Average name {average:.2f}")
    print("#### REPORT END ####")






def main():
    print("Program starting")
    print("This program analyses a list of names from a file.")
    DoStuff()
    print("Program end")
    return None

if __name__ == "__main__":
    main()