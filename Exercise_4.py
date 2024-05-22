#variables and names

# declaring variables.
car=100
space_in_car=4.0
drivers=30
passangers=90
#find cars not driven by suntracting cars by drivers
car_not_driven=car-drivers                        
car_driven=drivers
#find car capasity by multipling car driven and space in car
car_capasity=car_driven* space_in_car
#find avg passangers per car
avg_passangers_per_car=passangers/car_driven


#printing values
print("There are",car,"cars available")
print("There are only", drivers, "drivers available")
print("There will be",car_not_driven,"empty car today")
print("We can transport",car_capasity,"people today")
print("We have",passangers,"to carpool today")
print("we need to put about",avg_passangers_per_car,"in each car")



