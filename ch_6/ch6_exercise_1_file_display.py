"""
1. File Display
Assume a file containing a series of integers is named numbers.txt and exists on the computer’s
disk. Write a program that displays all of the numbers in the file.
"""


def main():
    read_numbers()


def read_numbers():
    file_name = 'numbers.txt'
    try:
        number_file = open(file_name, 'r')
        for number in number_file:
            print(number.strip())
    except IOError:
        print(f"Sorry. No '{file_name}' exists ")


main()
