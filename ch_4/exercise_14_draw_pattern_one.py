"""
14. Write a program that uses nested loops to draw this pattern:
*******
******
*****
****
***
**
*
"""
for row in range(7, 0, -1):
    for col in range(row, 0, -1):
        print("*", end="")
    print()
