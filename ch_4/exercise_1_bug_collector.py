"""
1. Bug Collector
A bug collector collects bugs every day for five days. Write a program that keeps a running
total of the number of bugs collected during the five days. The loop should ask for the
number of bugs collected for each day, and when the loop is finished, the program should
display the total number of bugs collected.
"""

DAYS = 5
current_day = 0
bugs_collected = 0
continue_collecting_bugs = True

while continue_collecting_bugs:
    if current_day == 5:
        continue_collecting_bugs = False
    else:
        try:
            bugs = int(input("How many bugs have you collected today: "))
            bugs_collected += bugs
        except:
            print("You have entered an invalid entry")
            continue
    current_day += 1
print(f"Bugs collected:", bugs_collected)

