#from car import Car, ElectricCar
import car

my_new_car = car.Car('audi', 'a6', 2020)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_new_tesla = car.ElectricCar('tesla', 't6', 2020)
print(my_new_tesla.get_descriptive_name())
