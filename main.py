from elevator import Elevator
from elevatorController import ElevatorController
from visualizer import Visualizer


# Runs elevator against various cases to determine overall efficiency
def main():

    elevator = Elevator(num_floors=5, starting_floor=3)
    controller = ElevatorController(elevator)
    #The following requests can come from different floors.
    controller.request_floor(current_floor=1, floor=4)
    controller.request_floor_from_inside(5)
    controller.request_floor(current_floor=2, floor=3)
    v = Visualizer()
    v.visualize(controller)

if __name__ == '__main__':
    main()
