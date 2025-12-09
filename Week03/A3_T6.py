"""A3_T6 Submenu (TEST TASK)
Create menu program with submenus. Mainly for unit conversions. Use the values from the following table for unit conversions https://www.isa.org/getmedia/192f7bda-c77c-480a-8925-1a39787ed098/CCST-Conversions-document.pdf

Menu options:

Length
Meters to kilometers
Kilometers to meters
Weight
Grams to pounds
Pounds to grams
Exit
“Exiting...”
Handle all the data in floating point datatype. Remember to round every value in 1 digit precision right before displaying.

Other possible prints:

“Unknown option.”
Example run - weight conversion 1

run 1 run 2 run 3 run 4 run 5 run 6 run 7 run 8 run 9
Program starting.
Welcome to the unit converter program!
Follow the menu instructions below.

Options:
1 - Length
2 - Weight
0 - Exit
Your choice: 1

Length options:
1 - Meters to kilometers
2 - Kilometers to meters
0 - Exit
Your choice: 1
Insert meters: 1000
1000.0 m is 1.0 km

Program ending.
"""
print("Program starting.")
print("Welcome to the unit converter program!")
print("Follow the menu instructions below.\n")

print("Options:")
print("1 - Length")
print("2 - Weight")
print("0 - Exit")

choice = int(input("Your choice: "))

if choice == 0:
    print("Exiting...")

elif choice == 1:
    print("\nLength options:")
    print("1 - Meters to kilometers")
    print("2 - Kilometers to meters")
    print("0 - Exit")

    length_choice = int(input("Your choice: "))

    if length_choice == 0:
        print("Exiting length menu...")
    elif length_choice == 1:
        meters = float(input("Insert meters: "))
        kilometers = meters / 1000
        print(f"{meters:.1f} m is {kilometers:.1f} km")
    elif length_choice == 2:
        kilometers = float(input("Insert kilometers: "))
        meters = kilometers * 1000
        print(f"{kilometers:.1f} km is {meters:.1f} m")
    else:
        print("Unknown option.")

elif choice == 2:
    print("\nWeight options:")
    print("1 - Grams to pounds")
    print("2 - Pounds to grams")
    print("0 - Exit")

    weight_choice = int(input("Your choice: "))

    if weight_choice == 0:
        print("Exiting weight menu...")
    elif weight_choice == 1:
        grams = float(input("Insert grams: "))
        pounds = grams / 453.59237
        print(f"{grams:.1f} g is {pounds:.1f} lb")
    elif weight_choice == 2:
        pounds = float(input("Insert pounds: "))
        grams = pounds * 453.59237
        print(f"{pounds:.1f} lb is {grams:.1f} g")
    else:
        print("Unknown option.")

else:
    print("Unknown option.")

print("\nProgram ending.")