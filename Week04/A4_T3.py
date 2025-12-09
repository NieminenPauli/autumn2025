"""A4_T3 While-loop
Make Python program which prompts user to insert two integers.
 Use these integers together with the “while-loop” structure to create
   behaviour like in the example program run below.

Note! the autograding tool will test that the correct structure has been applied.

Example program runs

run 1 run 2 run 3
Program starting.

Insert starting value: 1
Insert stopping value: 10

Starting while-loop:
1 2 3 4 5 6 7 8 9 10

Program ending."""

print("Program starting")
num1 = int(input("Insert starting value: "))
num2 = int(input("Insert stopping value: "))

print("Starting while loop")

i = num1
while i <= num2:
    if i < num2:
        print(i,end=" ")
    else:
        print(i)
    i +=1

print("\nProgram ending")
