"""A2_T7 Fahrenheit to Celcius
Create a Python program to convert Fahrenheit to Celcius.
 Round the Celsius to 1 decimal precision.

Formula to calculate Celcius from Fahrenheit is (Fahrenheit - 32) / 1.8

Example program run:

Program starting.
Insert fahrenheits: 50
50.0°F is 10.0°C
Program ending.
"""

print("Programn Starting")
farenheits = float(input("Insert fahrenheits: "))

celsius = (farenheits -32) /1.8

print(f"{farenheits} is {round(celsius,1)}")

print("Program ending")
