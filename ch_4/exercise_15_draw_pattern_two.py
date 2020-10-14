"""
15. Write a program that uses nested loops to draw this pattern:
##
# #
#  #
#   #
#    #
#     #
"""
for row in range(6):
    print("#", end='')
    for col in range(row):
        print(" ", end="")
    print("#")
