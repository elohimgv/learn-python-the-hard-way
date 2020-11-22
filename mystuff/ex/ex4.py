# total cars
cars = 100
# total space in a car
space_in_a_car = 4.0
# total drivers
drivers = 30
# total passangers
passengers = 90
# cars not used
cars_not_driven = cars - drivers
# cars to drive is equal to available drivers
cars_driven = drivers
# the carpool capacity is given by: cars_driven * space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
# the average passangers per car y given by: passengers / cars_driven
average_passangers_per_car = passengers / cars_driven

print("There are", cars, "cars available")
print("There are only", drivers, "drivers available")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put aobut", average_passangers_per_car, "in each car.")