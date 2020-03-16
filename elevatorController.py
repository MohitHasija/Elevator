from copy import copy


class ElevatorController(object):
    def __init__(self, elevator):
        # An unordered set of floor numbers that have been requested
        self.requested_floors = set()
        # An ordered list of floors that have been visited
        self.visited_floors = []
        # Number of floors traveled since the elevator was started
        self.num_floors_traveled = 0
        # current number of floor
        self.current_floor = elevator.current_floor
        # total number of eccessible floors by elevator
        self.num_floors = elevator.num_floors
    # Registers a request to visit a specific floor

    def validate_floor_call(self, floor):
        # This condition excludes negative and out of range floor values.
        return floor >= 0 and floor <= self.num_floors

    def request_floor_from_inside(self, floor):
        # This condition excludes negative and out of range floor values.
        if self.validate_floor_call(floor) and floor != self.current_floor:
            self.requested_floors.add(floor)

    def request_floor(self,current_floor, floor):
        if current_floor != floor and self.validate_floor_call(floor):
            self.requested_floors.add(floor)
            if current_floor != self.current_floor:
                self.requested_floors.add(current_floor)

    # Computes number of floors passed when traveling from the current floor to
    # the given floor (including the given floor itself)
    def get_floor_difference(self, floor):
        return abs(self.current_floor - floor)

    # Travels to the given floor to pick up or drop off passengers
    def visit_floor(self, floor):
        self.num_floors_traveled += self.get_floor_difference(floor)
        self.current_floor = floor
        self.visited_floors.append(self.current_floor)
        # discard() will not raise an exception if floor does not exist
        self.requested_floors.discard(self.current_floor)

    # Starts elevator and travels computed route according to current requests
    def travel(self):
        # Visit next closest requested floor until all requested floors have
        # been visited
        print("The floors to visit are:", self.requested_floors)
        while len(self.requested_floors) != 0:
            closest_floor = min(
                self.requested_floors, key=self.get_floor_difference)
            floor_to_visit = closest_floor
            if floor_to_visit == self.current_floor:
                copy_of_requested_floors = copy(self.requested_floors)
                copy_of_requested_floors.discard(self.current_floor)
                floor_to_visit = min(copy_of_requested_floors, key=self.get_floor_difference)
            print("The floor to visit is:", floor_to_visit)
            self.visit_floor(floor_to_visit)
