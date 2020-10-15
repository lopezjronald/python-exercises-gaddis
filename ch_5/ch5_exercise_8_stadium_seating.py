"""
7. Stadium Seating
There are three seating categories at a stadium. Class A seats cost $20, Class B seats cost
$15, and Class C seats cost $10. Write a program that asks how many tickets for each class
of seats were sold, then displays the amount of income generated from ticket sales.
"""


def ask_amount_sold(seat):
    while True:
        try:
            seats_sold = int(input(f"How many class {seat} seats were sold: "))
            return seats_sold
        except:
            print("You have entered an invalid entry")
            continue


def ask_class_a():
    return 20 * ask_amount_sold("A")


def ask_class_b():
    return 15 * ask_amount_sold("B")


def ask_class_c():
    return 10 * ask_amount_sold("C")


def display_total_income(class_a, class_b, class_c):
    print(f"Class A: ${class_a:,.0f}")
    print(f"Class B: ${class_b:,.0f}")
    print(f"Class C: ${class_c:,.0f}")
    print(f"Total Income Generated: ${sum([class_a, class_b, class_c]):,.0f}")


def main():
    class_a = ask_class_a()
    class_b = ask_class_b()
    class_c = ask_class_c()
    display_total_income(class_a, class_b, class_c)


main()
