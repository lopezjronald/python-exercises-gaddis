"""
11. Sleep Debt
A “sleep debt” represents the difference between a person’s desirable and actual amount
of sleep. Write a program that prompts the user to enter how many hours they slept each
day over a period of seven days. Using 8 hours per day as the desirable amount of sleep,
determine their sleep debt by calculating the total hours of sleep they got over the seven-day
period and subtracting that from the total hours of sleep they should have got. If the user
does not have a sleep debt, display a message expressing your jealousy.
"""
DAYS_IN_WEEK = 7
DESIRED_SLEEP = DAYS_IN_WEEK * 8
hours_slept = []

for hour in range(DAYS_IN_WEEK):
    while True:
        try:
            hours_slept.append(int(input("Hours slept: ")))
            break
        except:
            print("Invalid entry")
            continue

if sum(hours_slept) < DESIRED_SLEEP:
    print(f"Sleep: How dare you neglect me! You only slept {sum(hours_slept)}! You are {DESIRED_SLEEP - sum(hours_slept)} hours short of sleep!")
else:
    print(f"Thank you for sleeping {sum(hours_slept)} hours this week.")
