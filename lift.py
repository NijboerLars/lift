class Lift:

    def __init__(self):
        self.current_floor = 0
        self.customers_inside = 0
        self.top_reached = False

    def move_up(self):
        self.current_floor += 1
        print('Lift has moved up to floor ' + str(self.current_floor))

    def move_down(self):
        self.current_floor -= 1
        print('Lift has moved down to floor ' + str(self.current_floor))

    def increase_customers_inside(self):
        self.customers_inside += 1

    def decrease_customers_inside(self):
        self.customers_inside -= 1

    def get_customers_inside(self):
        return self.customers_inside
        print(self.customers_inside + ' customers inside the lift.')
