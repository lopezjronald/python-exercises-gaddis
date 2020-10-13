"""
2. Calories Burned
Running on a particular treadmill you burn 4.2 calories per minute. Write a program that
uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30 minutes.
"""

minutes = [10, 15, 20, 25, 30]
CALORIES_BURNED = 4.2
for mins in minutes:
    print(f"{mins} minutes burns {mins * CALORIES_BURNED} calories.")