#UNWSP Programming PythonCos2005DEsp25
#Program_2_Car Class
#04.4.25
#Abraham. N. Andersen

class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed

my_car = Car(2020, "Peoplescar")
#cause Volkswagon
print("Car speeds up:")
for _ in range(5):
    my_car.accelerate()
    print(f"Current speed: {my_car.get_speed()}")

print("\nCar slows down:")
for _ in range(5):
    my_car.brake()
    print(f"Current speed: {my_car.get_speed()}")