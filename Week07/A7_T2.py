




def UserInput():
    integers = []

    feed = input("Insert comma separated integers: ")

    fixed = feed.split(",")

    for i in fixed:
        i = i.strip()
        try:
            num = int(i)
            integers.append(i)
        except:
            print(f"Error: '{i}' is not valid integer")
        
    
    print(f"Valid integers: {integers}")
    integers = [int(x) for x in integers]
    sum = 0
    for i in integers:
        sum += i
    
    print(f"There are {len(integers)}´in the list")
    if sum % 2:
        print(f"Sum of the integers is {sum} an it's even")

    else:
        print(f"Sum of the integers is {sum} an it's odd")
    return None






def main():
    print("Program starting.")
    UserInput()
    print("Program stopping")
    return None


if __name__ == "__main__":
    main()