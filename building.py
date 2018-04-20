class Building:

    def __init__(self, number_of_floors):
        self.number_of_floors = number_of_floors

    @property
    def get_number_of_floors(self):
        return self.number_of_floors
