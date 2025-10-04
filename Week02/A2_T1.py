"""A2_T1: Basic program structure
Make a Python program, which prompts the user name and two floating numbers. Multiply the inserted numbers to get product. Round the product in two decimal precision. Complete the program output as shown below.

Example program run:

Program starting.
What is your name: John
Enter a floating point number: 3.1
Enter second floating point number: 5.3
John you gave numbers 3.1 and 5.3
Multiplying first and second number will result in product 16.43
Program ending.
"""
Name = input("What is your name: ")
Feed = input("Enter the floating point numner: ")
Num1 = float(Feed)
Feed = input("Enter second floating point number: ")
Num2 = float(Feed)
Product = Num1 * Num2

print(f"{Name} you gave numbers {Num1} and {Num2}")
print(f"Multiplying first and second number will result in product {Product:.2f}")
print("Multiplying first and second number will result in product",round(Product,2))
print("Program Ending")