from elevator import Direction
from elevator import RequestsLL
from elevator import Elevator

from time import sleep

def RequestLLTests():
    asc_requests = RequestsLL(Direction.Ascending)
    des_requests = RequestsLL(Direction.Descending)

    asc_requests.add(1)
    asc_requests.add(4)
    asc_requests.add(2)

    assert asc_requests.array == [1, 2, 4]

    asc_requests.remove()
    asc_requests.add(7)
    asc_requests.add(5)

    assert asc_requests.array == [2, 4, 5, 7]

    print "Ascending tests passed."

    des_requests.add(4)
    des_requests.add(2)
    des_requests.add(9)
    des_requests.add(6)

    assert des_requests.array == [9, 6, 4, 2]
    
    des_requests.remove()
    des_requests.remove()
    des_requests.add(12)

    assert des_requests.array == [12, 4, 2]

    print "Descending tests passed."

def ElevatorTests():
    print ""
    print "-----Elevator Tests Starting------"
    elevator = Elevator()
    elevator.start()

    elevator.add_request(4)
    elevator.add_request(7)
    elevator.add_request(3)
    elevator.add_request(9)

    sleep(5)

    elevator.add_request(3)
    elevator.add_request(5)
    elevator.add_request(2)

    sleep(5)

    elevator.add_request(10)
    elevator.add_request(14)

    sleep(5)

    print "-----Elevator Tests Passed-------"

RequestLLTests()
ElevatorTests()
