"""
12. Average Steps Taken
A Personal Fitness Tracker is a wearable device that tracks your physical activity, calories
burned, heart rate, sleeping patterns, and so on. One common physical activity that most
of these devices track is the number of steps you take each day.
If you have downloaded this book’s source code from the Premium Companion Website,
you will find a file named steps.txt in the Chapter 06 folder. (The Premium Companion
Website can be found at www.pearsonglobaleditions.com/gaddis.) The steps.txt file
contains the number of steps a person has taken each day for a year. There are 365 lines
in the file, and each line contains the number of steps taken during a day. (The first line is
the number of steps taken on January 1st, the second line is the number of steps taken on
January 2nd, and so forth.) Write a program that reads the file, then displays the average
number of steps taken for each month. (The data is from a year that was not a leap year,
so February has 28 days.)
"""


def create_tracker_file():
    new_file = open('tracker.txt', 'w')
    return new_file


def close_file(file):
    file.close()


def random_steps():
    import random
    return random.randint(100, 5000)


def record_steps_in_file(filename):
    days_of_month = {
        'jan': 31,
        'feb': 28,
        'mar': 31,
        'apr': 30,
        'may': 31,
        'jun': 30,
        'jul': 31,
        'aug': 31,
        'sept': 30,
        'oct': 31,
        'nov': 30,
        'dec': 31
    }
    tracker = step_tracker(days_of_month)
    for day, steps in tracker.items():
        print(f"{day.title()}: {steps:,.0f} steps")
        filename.write(f"{day.title()}\t{steps:,.0f}\n")


def step_tracker(month_and_day):
    tracker = {}
    for month, days in month_and_day.items():
        for day in range(1, days + 1):
            tracker[f"{month} {day}"] = random_steps()
    return tracker


def main():
    new_file = create_tracker_file()
    record_steps_in_file(new_file)
    close_file(new_file)


main()
