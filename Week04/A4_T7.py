print("Program starting.\n")
print("Check multiplicative persistence.")

number = input("Insert an integer: ")

steps = 0

while len(number) > 1:
    product = 1
    i = 0
   
    while i < len(number):
        product *= int(number[i])
        i += 1


    i = 0
    while i < len(number):
        print(number[i], end="")
        if i < len(number) - 1:
            print(" * ", end="")
        i += 1
    print(" = " + str(product))

    number = str(product)
    steps += 1

print("No more steps.\n")
print(f"This program took {steps} step(s)\n")
print("Program ending.")