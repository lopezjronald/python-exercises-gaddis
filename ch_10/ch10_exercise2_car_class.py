"""
2. Car Class
Write a class named Car that has the following data attributes:
• _ _year_model (for the car’s year model)
• _ _make (for the make of the car)
• _ _speed (for the car’s current speed)
The Car class should have an _ _init_ _ method that accepts the car’s year model and
make as arguments. These values should be assigned to the object’s _ _year_model and
_ _make data attributes. It should also assign 0 to the _ _speed data attribute.
The class should also have the following methods:
• accelerate
The accelerate method should add 5 to the speed data attribute each time it is called.
• brake
The brake method should subtract 5 from the speed data attribute each time it is called.
• get_speed
The get_speed method should return the current speed.
Next, design a program that creates a Car object then calls the accelerate method five
times. After each call to the accelerate method, get the current speed of the car and display
it. Then call the brake method five times. After each call to the brake method, get the
current speed of the car and display it.
"""


class Car:

    def __init__(self, make, model, year_model, speed):
        self.__make = make
        self.__model = model
        self.__year_model = year_model
        self.__speed = speed

    def __str__(self):
        return f"Make: {self.__make}\n" \
               f"Model: {self.__model}\n" \
               f"Year: {self.__year_model}\n" \
               f"Speed: {self.__speed}"

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year_model(self):
        return self.__year_model

    def get_speed(self):
        return self.__speed

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_year_model(self, year):
        self.__year_model = year

    def set_speed(self, speed):
        self.__speed = speed

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5


def main():
    car_make = input("What is the car make: ")
    car_model = input("What is the car model: ")
    car_year = input(f"What is the {car_make} year: ")
    car_speed = None
    while True:
        try:
            car_speed = float(input("What is the car speed: "))
            break
        except ValueError:
            print("Invalid entry")
            continue
    new_car = Car(car_make, car_model, car_year, car_speed)
    print(new_car)
    speeding = True
    while speeding:
        accelerate_or_brake(new_car)
        while True:
            continue_speeding = input("Would you like to continue ('y' for yes 'n' for no)\n")
            if continue_speeding.lower() == 'y':
                break
            elif continue_speeding.lower() == 'n':
                speeding = False
                break
            else:
                print("Invalid entry")


def accelerate_or_brake(car_object):
    while True:
        choice = input("1: Accelerate\n2: Brake\n")
        try:
            choice = int(choice)
        except ValueError:
            print("Invalid entry")
            continue
        if choice == 1:
            car_object.accelerate()
        elif choice == 2:
            car_object.brake()
        else:
            print("Invalid Entry")
            continue
        print(f"Car Speed: {car_object.get_speed()}")
        break


main()
