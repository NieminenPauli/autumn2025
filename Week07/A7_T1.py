

def CollectUserData():
    integers = []
    

    while True:
        try:
            num =int(input("Insert positive integer(negative stops): "))
            if(num>=0):
                integers.append(num)
            if(num<0):
                break
        except:
            print("You need to give an integer")
    
    print(f"Displaying {len(integers)} integers:")
    index = 0
    ordinal = 1
    for i in integers:
        print(f"Index {index} => Ordinal {ordinal} => Integer {i}")
        index +=1
        ordinal+=1






def main():
    print("Program starting.")
    print("Collect positive integers")
    CollectUserData()
    print("Program stopping")

    return None

if __name__ == "__main__":
    main()