"""
4. Distance Traveled
The distance a vehicle travels can be calculated as follows:

distance = speed x time

For example, if a train travels 40 miles per hour for three hours, the distance traveled is
120 miles. Write a program that asks the user for the speed of a vehicle (in miles per hour)
and the number of hours it has traveled. It should then use a loop to display the distance
the vehicle has traveled for each hour of that time period. Here is an example of the desired
output:

What is the speed of the vehicle in mph? 40 Enter

How many hours has it traveled? 3 Enter

Hour    Distance Traveled
1       40
2       80
3       120
"""

hour = None
distance = None
while True:
    try:
        hour = int(input("Hour: "))
    except:
        print("Invalid entry")
        continue
    break

while True:
    try:
        distance = float(input("Distance: "))
    except:
        print("Invalid entry")
        continue
    break
print("Hour\tDistance Traveled")
for each_hour in range(1, hour+1):
    print(f"{each_hour}\t\t{each_hour * distance:,.2f}")

