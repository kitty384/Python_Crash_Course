# from car import EletricCar,Car

# my_tesla = EletricCar("tesla", "model s", 2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.get_range()
# my_tesla.battery.upgrade_battery()
# my_car=Car("audi","a4",2016)
# print(my_car.get_descriptive_name())

import car
my_tesla = car.EletricCar("tesla", "model s", 2016)
print(my_tesla.get_descriptive_name())

my_beetle = car.Car("volkswagen", "beetle", 2016)
print(my_beetle.get_descriptive_name())
