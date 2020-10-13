"""
3. Lap Times
Write a program that asks the user to enter the number of times that they have run around
a racetrack, and then uses a loop to prompt them to enter the lap time for each of their laps.
When the loop finishes, the program should display the time of their fastest lap, the time of
their slowest lap, and their average lap time.
"""

import numpy as np

laps = None
times = []

still_running = True
while still_running:
    try:
        laps = int(input("How many laps did you run: "))
        still_running = False
    except:
        print("You have entered an invalid entry")
        continue

for lap in range(laps):
    still_running = True
    while still_running:
        try:
            times.append(float(input("Please enter your time (ex: 2.34)")))
            still_running = False
        except:
            print("Invalid entry")
            continue

print(f"Fastest Lap: {min(times)}")
print(f"Slowest Lap: {max(times)}")
print(f"Average Lap: {np.mean(times):,.2f}")

