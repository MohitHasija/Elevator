# Elevator class which implements an algorithm for controlling the
# decision-making logic of an elevator (i.e. deciding which floor to go next)
class Elevator(object):

    # Initializes a new Elevator object
    def __init__(self, num_floors, starting_floor):
        # Total number of floors accessible by the elevator
        self.num_floors = num_floors
        # Current floor number
        self.current_floor = starting_floor
