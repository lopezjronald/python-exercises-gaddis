"""
1. Kilometer Converter
Write a program that asks the user to enter a distance in kilometers, then converts that
distance to miles. The conversion formula is as follows:

Miles = Kilometers x 0.6214
"""


def km_to_miles():
    while True:
        try:
            kilometers = float(input("Please enter kilometer distance you would like to convert to miles: "))
            miles = kilometers * 0.6214
            return f"{kilometers} kilometers is converted to {miles} miles."
        except:
            print("Invalid Entry")

print(km_to_miles())


