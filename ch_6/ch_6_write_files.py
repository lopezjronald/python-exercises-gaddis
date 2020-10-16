# How to open a file

# file_variable = open(filename, mode)
# • file_variable is the name of the variable that will reference the file object.
# • filename is a string specifying the name of the file.
# • mode is a string specifying the mode (reading, writing, etc.) in which the file will be
# opened.
#
# Mode Description
# 'r': Open a file for reading only. The file cannot be changed or written to.
# 'w': Open a file for writing. If the file already exists, erase its contents. If it does
# not exist, create it.
# 'a': Open a file to be written to. All data written to the file will be appended to its
# end. If the file does not exist, create it.
#
# open a file in a different location: example below
# test_file = open(r'C:\Users\lopez\Desktop\code\etc\etc


# customer_file = open('customers.txt', 'r')
# for content in customer_file:
#     print(content)
#
# sales_file = open('sales.txt', 'w')


def main():
    # Open a file named philosophers.txt.
    outfile = open('philosophers.txt', 'w')
    # Write the names of three philosphers
    # to the file.
    outfile.write('John Locke\n')
    outfile.write('David Hume\n')
    outfile.write('Edmund Burke\n')

    # Close the file.
    outfile.close()

# Call the main function.
main()
