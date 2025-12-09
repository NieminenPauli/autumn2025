#open file
#copy to other file 

# choose from 
# choose where

def  WorkWithFile(source,destination: str):
    readFile = open(f"Week06/{source}","r")
    writeFile = open(f"Week06/{destination}","w")

    while True:
        line = readFile.readline()
        if len(line) == 0:
            break
        writeFile.write(line)
        
    print(f"Reading file {source} {line}")
    print("File content ready in memory.")
    print(f"Writing content into file {destination}")
    readFile.close()
    writeFile.close()
    print("Copying operation complete")


    return None

def DefineFilePath():
    sourceName = input("Insert source filename: ")
    destinationName = input("Insert destination filename: ")
    WorkWithFile(sourceName,destinationName)
    return None

def main():
    print("Program Starting")
    DefineFilePath()
    print("Program ending")

    return None
if __name__ == "__main__":
    main()