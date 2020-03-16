# Elevator
A sample elevator program that takes call from floors as well as inside elevator and runs the elevator.

The main function runs a sample elevator run to determine accuracy.
The ElevatorController class contains two methods.
  -- to add a lift service request from inside(request_floor_from_inside). It takes the requested floor as argument.
  -- to add a lift service request from any floor outside the lift(request_floor). It takes the current_floor_of_request and requested floor as an argument.
The tests are added to determine various cases accuracy and effeciency.
The visualiser helps to visualise the run by outputting print statements.

The usage is as follows:

Packages required:
copy, nose, unittest

1. python main.py (to run sample elevator run)
2. python tests.py (to run different tests)
