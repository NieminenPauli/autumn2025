"""A2_T6 Hex Colors (TEST TASK)
Write a Python program which asks user to insert hex color.
 In this case hex color is expected to be the 7 character representation
   starting with # and followed by 6 0-F characters to represent RGB colors.
     More about hex colors at https://en.wikipedia.org/wiki/Web_colors

Slice the amount of red, green and blue from that inserted color and display each color as shown below.

Example program run:

Program starting.

Insert a hex color: #FFA500

Colors
- Red FF
- Green A5
- Blue 00

Program ending."""

print("Program starting")
hexColor = input("Insert a hex color: ")

red = hexColor[1:3:1]
green = hexColor[3:5:1]
blue = hexColor[5:7:1]

print(f"- Red {red}")
print(f"- Green {green}")
print(f"- Blue {blue}")

print("Program ending")