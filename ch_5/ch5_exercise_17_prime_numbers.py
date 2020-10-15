def is_prime(number):
    prime_number = True
    half = int(1 + number / 2)
    while prime_number:
        for i in range(2, half):
            if number % i == 0:
                prime_number = False
        break
    return prime_number


def request_number():
    while True:
        try:
            return int(input("Enter Integer to Verify Whether Number is Prime: "))
        except:
            print("Invalid Entry")
            continue


def display_result(number):
    result = None
    if not is_prime(number):
        result = ' not '
    else:
        result = ' '
    print(f"{number} is{result}a prime number.")


def main():
    requested_number = request_number()
    display_result(requested_number)

