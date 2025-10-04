"""A2_T2: Escape sequence and print parameters
Make a Python program, which prompts user for a car brand and model. After user inputs, do print the car brand and model sentence with two print commands using “sep” and “end” parameters.

Example program run:

Program starting.
Insert car brand: Toyota
Insert car model: Corolla
Car brand is "Toyota" and the model is 'Corolla'.
Program ending."""

print("Program starting.")
brand= input("Insert car brand: ")
model = input("Insert car model: ")


print(f'Car Brand is "{brand}"',end=" ", sep=" ")
print(f'and the model is "{model}".')
print("program Ending")
