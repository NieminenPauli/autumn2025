#Write text file

#first name
#last name

#filename
def OpenFile(a,b,c):
    fileName = c
    lastName = b
    firstName = a

    file = open(f"Week06/{fileName}","w")
    file.write(f"{firstName}\n")
    file.write(f"{lastName}")
    file.close()


    return None

def askName():
    firstName = input("Insert first name: ")
    lastName  = input("Insert last name: ")
    fileName = input("Insert filename: ")
    OpenFile(firstName,lastName,fileName)

    return None

def main():
    print("Program starting")
    askName()
    print("Program ending")
    return None

if __name__ == "__main__":
    main()