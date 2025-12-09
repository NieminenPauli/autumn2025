"""A4_T2 For-loop 2
Copy the previous program and modify the behaviour to match the example program run below.
 This program must use “for-loop” structure.

It is recommended to replace the print-command end character with space,
 so that all the iterations can be printed on the same row.
   Last iteration might require additional logic to get rid of the extra space at the end.

Note! the autograding tool will test that the correct structure has been applied.

Example program runs

run 1 run 2 run 3
Program starting.

Insert starting value: 11
Insert stopping value: 15

Starting for-loop:
11 12 13 14 15

Program ending.

"""

#kopioitu edellisestä
print("Program starting.")
num1 = int(input("Insert starting value: "))
num2 = int(input("Insert stopping value: "))

print("Starting for loop")

for i in range(num1, num2 +1):
    print(i, end= " ")

print("\nProgram ending")