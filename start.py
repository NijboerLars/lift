from building import Building
from lift import Lift
from customer import Customer

number_of_floors = input('How many floors are there in the building? ')
while number_of_floors != int(number_of_floors) and int(number_of_floors) < 0:
    number_of_floors = input('Wrong input. Please enter a positive integer for number of floors: ')
number_of_floors = int(number_of_floors)

number_of_customers = input('How many customers are there? ')
while number_of_customers != int(number_of_customers) and int(number_of_customers) < 0:
    number_of_customers = input('Wrong input. Please enter a positive integer for number of customers: ')
number_of_customers = int(number_of_customers)

building = Building(number_of_floors)
lift = Lift()

customers = []

i = 1
for c in range(number_of_customers):
    """
    Create list of customer objects with an id, start floor and stop floor.
    """
    c = Customer(i)
    c.set_start_floor(number_of_floors)
    c.set_stop_floor(number_of_floors)
    customers.append(c)
    i += 1


print('Lift program started!\n')
while lift.top_reached == False:
    """
    Following code is run until the lift reaches the top floor.
    """
    while lift.current_floor < number_of_floors-1:
        for i in customers:
            """
            For every customer, check if their start and stop floor
            is equal to the lift's current floor. If there is a match,
            perform the required action.
            """
            if i.start_floor == lift.current_floor:
                i.get_in_lift()
                lift.increase_customers_inside()
            if i.stop_floor == lift.current_floor:
                i.get_out_lift()
                lift.decrease_customers_inside()
        lift.get_customers_inside()
        lift.move_up()
    lift.top_reached = True
"""
One more loop for the top floor itself.
"""
for i in customers:
    if i.start_floor == lift.current_floor:
        i.get_in_lift()
        lift.increase_customers_inside()
    if i.stop_floor == lift.current_floor:
        i.get_out_lift()
        lift.decrease_customers_inside()
lift.get_customers_inside()
lift.move_down()
"""
Now run the following code until the lift has reached floor 0.
"""
while lift.current_floor != 0:
    for i in customers:
        if i.stop_floor == lift.current_floor:
            i.get_out_lift()
            lift.decrease_customers_inside()
    lift.get_customers_inside()
    lift.move_down()
"""
One more loop for floor 0.
"""
for i in customers:
    if i.stop_floor == lift.current_floor:
        i.get_out_lift()
        lift.decrease_customers_inside()
lift.get_customers_inside()
print('\nLift program finished!')
