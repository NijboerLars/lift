from random import randint

class Customer:

    def __init__(self, id):
        self.id = id
        self.start_floor = None
        self.stop_floor = None
        self.in_lift = False
        self.destination_reached = False

    def set_start_floor(self, x):
        """
        Set random start floor in range of 0 to number of floors.
        """
        floors = range(x)
        y = randint(floors[0], floors[x-1])
        self.start_floor = y

    def set_stop_floor(self, x):
        """
        Set random stop floor in range of 0 to number of floors.
        Stop floor cannot be equal to start floor.
        """
        floors = range(x)
        y = randint(floors[0], floors[x-1])
        while y == self.start_floor:
            y = randint(floors[0], floors[x-1])
        self.stop_floor = y

    def get_in_lift(self):
        """
        Customer can enter the lift as long as they aren't currently in the lift,
        and their destination floor hasn't been reached.
        """
        if self.in_lift == False and self.destination_reached == False:
            self.in_lift = True
            print('Customer ' + str(self.id) + ' has entered the lift.')
        else:
            pass

    def get_out_lift(self):
        """
        People can exit the lift as long as they are currently in the lift.
        """
        if self.in_lift == True:
            self.in_lift = False
            print('Customer ' + str(self.id) + ' has exited the lift.')
            self.destination_reached = True
        else:
            pass
