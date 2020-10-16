"""
1. Valid Number Information
Design a program that uses a loop to build a list named valid_numbers that contains only
the numbers between 0 and 100 from the numbers list below. The program should then
determine and display the total and average of the values in the valid_numbers list.
"""


def list_of_random_numbers():
    import random
    number_list = []
    while True:
        try:
            for i in range(int(input("How many random numbers would you like to generate: "))):
                number_list.append(random.randint(-100, 200))
            return number_list
        except ValueError:
            print("Invalid Entry")
            continue


def valid_numbers(list_of_nums):
    print(list_of_nums)
    valid_numbers = []
    for valid_number in list_of_nums:
        if 0 <= valid_number <= 100:
            valid_numbers.append(valid_number)
    return valid_numbers


def display_valid_numbers(valid_numbers):
    print(f"Valid Numbers: {valid_numbers}")
    print(f"Average: {sum(valid_numbers) / len(valid_numbers):,.3f}")


def main():
    numbers = list_of_random_numbers()
    valid_num = valid_numbers(numbers)
    display_valid_numbers(valid_num)


main()
