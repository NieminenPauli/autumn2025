"""A4_T5 Break and continue
Make a program, which prompts user to insert three integers:

Starting point
Stopping point
Inspection point
Test the points with following rules(Note! testing order matters):

Starting point must be less than stopping point
"Starting point value must be less than the stopping point value."
The inspection point must be within the range of the start and stop points.
"Inspection value must be within the range of start and stop."
If any rule above is broken, print the violation message(s) to the user and then
 skip the next part till the "Program ending." print.

Run two for-loops like shown in the example program runs if none of the rules
 above are broken. Inside the loops, compare the inspection point to the current
   iteration. Use break and continue commands if the current iteration is same as 
   the inspection point. Otherwise print the current iteration on the same line.

Note! There must be no trailing space character at the end of any row.

Example program runs

run 1 run 2 run 3 run 4 run 5 run 6
Program starting.

Insert starting point: 3
Insert stopping point: 8
Insert inspection point: 5

First loop - inspection with break:
3 4
Second loop - inspection with continue:
3 4 6 7

Program ending."""
print("Program starting")
startingPoint = int(input("\nInsert starting point"))
stoppingPoint = int(input("Enter stopping point"))
inspectionPoint = int(input("Enter inspection point"))

error = False

#"Starting point value must be less than the stopping point value."
if startingPoint >= stoppingPoint:
    error = True
    print("Starting point value must be less than the stopping point value.")
#"Inspection value must be within the range of start and stop."
if  inspectionPoint < startingPoint and inspectionPoint > stoppingPoint:
    error = True
    print("Inspection value must be within the range of start and stop.")

if not error:
    print("\First loop - inspection with break:")
    first = False
    for i in range(startingPoint, stoppingPoint):
        if i == inspectionPoint:
            break
        if first:
            print(" ", end ="")
        print(i,end="")
        first=True
    print()

    print("Second loop - inspection with continue:")
    first = False
    for i in range(startingPoint, stoppingPoint):
        if i == inspectionPoint:
            continue
        if first:
            print(" ", end ="")
        print(i,end="")
        first=True
    print()
