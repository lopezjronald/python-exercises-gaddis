"""
2. File Head Display
Write a program that asks the user for the name of a file. The program should display only
the first five lines of the file’s contents. If the file contains less than five lines, it should
display the file’s entire contents.
"""


def main():
    file_name = ask_filename()
    display_file_content(file_name)


def ask_filename():
    file_name = input("What is the file name: ")
    return f"{file_name}.txt"


def read_file(file):
    try:
        return open(file, 'r')
    except:
        print(f"Sorry. {file} does not exist")



def display_file_content(file):
    file_content = read_file(file)

    for i in range(5):
        content = file_content.readline()
        if content.strip() == '':
            break
        else:
            print(str(content.strip()))


main()
