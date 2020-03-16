from time import sleep

class Visualizer(object):
    # Tests the elevator by running it and outputting statistics
    # This function assumes that floors have already been requested
    def visualize(self,Controller):

        # Output initial parameters and state of elevator
        print('Number of floors: {}'.format(Controller.num_floors))
        print('Starting at floor {}'.format(Controller.current_floor))
        print('Requested floors: {}'.format(
            ', '.join(map(str, Controller.requested_floors))))
        Controller.travel()
        # Output statistics pertaining to elevator's completed journey
        print('Visited floors: {}'.format(
            ', '.join(map(str, Controller.visited_floors))))
        print('Number of floors traveled: {}'.format(Controller.num_floors_traveled))
