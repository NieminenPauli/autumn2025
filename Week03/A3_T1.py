"""A3_T1 If-statements
Make Python program and implement if-statements in proper places.

Ask user to insert two integers
Compare the integers and then announce the greater number
Create sum of the two integers
Check the parity of the sum (see modulo-operator ‘%’)
Other possible output variants:

Integer comparison
Integers are the same.
First integer is greater.
Parity check
Sum is even.
Example program run

run 1 run 2 run 3
Program starting.
Insert two integers.
Insert first integer: 5
Insert second integer: 5
Comparing inserted integers.
Integers are the same

Adding integers together
5 + 5 = 10

Checking the parity of the sum...
Sum is even.
Program ending.
"""
print("Program is starting")
print("Insert two integers")

num1 = int(input("Insert first integer: "))
num2 = int(input("Insert second integer"))

print("Comparing inserted integers")

if num1 == num2:
    print("Integers are the same")
elif num1 > num2:
    print(f"Int 1 is greater {num1}")

else:
    print(f"int2 is greater {num2}")


sum = num1 + num2
print("Adding integers together")
print(f"{num1} + {num2} = {sum}")

print("Checking the parity of the sum...")

if sum % 2 ==0 :
    print("Sum is even")
else:
    print("Sum is not even")
