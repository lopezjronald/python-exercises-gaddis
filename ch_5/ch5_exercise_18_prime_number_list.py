from ch_5 import ch5_exercise_17_prime_numbers as prime_numbers

for number in range(101):
    print(f"{number} prime: {prime_numbers.is_prime(number)}")