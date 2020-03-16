import nose.tools as noset
import unittest
from elevator import Elevator
from elevatorController import ElevatorController


class ElevatorTests(unittest.TestCase):

    def setUp(self):
        elevator = Elevator(num_floors=5, starting_floor=2)
        self.controller = ElevatorController(elevator)

    def test_init_params(self):
        """should store correct initial parameters when elevator is initalized"""
        controller = self.controller
        noset.assert_equal(controller.num_floors, 5)
        noset.assert_equal(controller.current_floor, 2)
        noset.assert_set_equal(controller.requested_floors, set())
        noset.assert_list_equal(controller.visited_floors, [])
        noset.assert_equal(controller.num_floors_traveled, 0)

    def test_request_floor(self):
        """should register requested floors"""
        controller = self.controller
        controller.request_floor(2, 3)
        controller.request_floor(4, 5)
        noset.assert_set_equal(controller.requested_floors, {3, 4, 5})

    def test_visited_floors(self):
        """should register visited floors in order"""
        controller = self.controller
        controller.request_floor(1, 4)
        controller.request_floor(4, 2)
        controller.travel()
        noset.assert_list_equal(controller.visited_floors, [1, 2, 4])


    def test_num_floors_traveled_up(self):
        """should keep track of the number of floors traveled going up"""
        controller = self.controller
        controller.request_floor(2, 5)
        controller.travel()
        noset.assert_equal(controller.num_floors_traveled, 3)

    def test_num_floors_traveled_down(self):
        """should keep track of the number of floors traveled going down"""
        controller = self.controller
        controller.request_floor(2, 1)
        controller.travel()
        noset.assert_equal(controller.num_floors_traveled, 1)

    def test_num_floors_traveled_up_down(self):
        """should keep track of the number of floors traveled going up then down"""
        controller = self.controller
        controller.request_floor(1, 5)
        controller.request_floor(3, 1)
        controller.travel()
        noset.assert_equal(controller.num_floors_traveled, 5)

    def test_minimize_retrace(self):
        """should minimize the retracing of the elevator's path"""
        controller = self.controller
        controller.request_floor(2, 4)
        controller.request_floor(2, 5)
        controller.request_floor(2, 3)
        controller.request_floor(2, 2)
        controller.travel()
        noset.assert_list_equal(controller.visited_floors, [3, 4, 5])

    def test_floor_value_greater_than_highest_floor(self):
        """should gracefully ignore invalid floor requests"""
        controller = self.controller
        controller.request_floor(1, 7)
        controller.request_floor(1, -1)
        controller.request_floor(2, 3)
        noset.assert_set_equal(controller.requested_floors, {3})
        controller.travel()
        noset.assert_list_equal(controller.visited_floors, [3])


if __name__=='__main__':
    unittest.main()
