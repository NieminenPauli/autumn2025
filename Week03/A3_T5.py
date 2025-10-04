"""A3_T5 Temperature converter (TEST TASK)
Create a temperature unit conversion program.

Start the program by listing options for the user:

Celsius to Fahrenheit
Fahrenheit to Celsius
Exit
Prompt user to insert choice. After the decision to convert, ask the amount of current temperature (use the floating point datatype). Lastly show the converted value to the user.

For the unit conversions, use the formula Celsius = (Fahrenheit - 32) / 1.8

Data representation examples:

50.0 °F
10.0 °C
If the user chooses option Exit, notify the user: Exiting...

Use 1 decimal precision to round the converted value.

Example program runs

run 1 run 2 run 3
Program starting.

Options:
1 - Celsius to Fahrenheit
2 - Fahrenheit to Celsius
0 - Exit
Your choice: 1
Insert the amount of Celsius: 23
23.0 °C equals to 73.4 °F

Program ending.

"""
print("Program starting")
print("Options:")
print("1 - Celsius to Fahrenheit")
print("2 - Fahrenheit to Celsius")
print("0 - Exit")
choice = int(input("Your choice: "))



if choice == 0:
    print("Exiting...")
elif choice == 1:
    celcius = float(input("Insert the amount of Celcius: "))
    fahrenheit = (celcius * 1.8) +32
    print(f"{celcius}°C equals to {fahrenheit}°F")
elif choice == 2:
    fahrenheit = float(input("Insert the amount of fahrenheit: "))
    celcius = (fahrenheit +32) /1.8
    print(f"{fahrenheit}°F equals to {celcius}°C")
elif choice == 0:
    print("Exiting...")


print("Program ending")