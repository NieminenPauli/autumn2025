"""A2_T4: Average and rounding
Prompt the user to insert the minutes spent on each previous 
topic task. Calculate the sum and the average. Display those
 in the example program run format(Note! precision). 
 Make sure to calculate the required average for two decimal
   digits and later integer as rounded integer
     (precision 0 + type conversion).

Example program run:

Program starting.
Estimate how many minutes you spent on programming...

A1_T1: 3
A1_T2: 7
A1_T3: 9
A1_T4: 8
A1_T5: 13
A1_T6: 14
A1_T7: 21

In total you spent 75 minutes on programming.
Average per task was 10.71 min and same rounded to the nearest integer 11 min.

Program ending."""

print("Program starting")
print("Estimate how many minutes you spent on programming...")
T1 = input("A1_T1: ")
T2 = input("A1_T2: ") 
T3 = input("A1_T3: ")
T4 = input("A1_T4: ")
T5 = input("A1_T5: ")
T6 = input("A1_T6: ")
T7 = input("A1_T7: ")

sum = float(T1) + float(T2) + float(T3) + float(T4) + float(T5) + float(T6) + float(T7)
average = sum / 7
rounded = int(average)

print(f"In total you spent {sum} on programming")
print(f"Average per task was {round(average,2)} min anf same rounded to the nearest integer {rounded} min")