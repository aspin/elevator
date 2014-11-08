from enum import Enum
from threading import Thread

class Direction(Enum):
    Ascending = 1
    Descending = 2
    Stationary = 3

class RequestsLL:

    def __init__(self, direction):
        self.array = []
        if direction == Direction.Ascending:
            self.direction = 1
        else:
            self.direction = -1

    def add(self, requested):
        for i in range(len(self.array)+1):
            if (i == len(self.array)) or (self.array[i] * self.direction > requested * self.direction):
                break

        self.array.insert(i, requested)

    def remove(self):
        self.array.pop(0)

    def length(self):
        return len(self.array)


class Elevator:

    def __init__(self):
        self.current = 1
        self.direction = Direction.Stationary
        self.asc_requests = RequestsLL(Direction.Ascending)
        self.des_requests = RequestsLL(Direction.Descending)

    def add_request(self, requested):
        if requested > self.current:
            self.asc_requests.add(requested)
            if self.direction == Direction.Stationary:
                self.direction = Direction.Ascending
        else:
            self.des_requests.add(requested)
            if self.direction == Direction.Stationary:
                self.direction = Direction.Descending

    def move(self):
        if self.direction == Direction.Ascending:
            selector = self.asc_requests
        else:
            selector = self.des_requests

        while (self.asc_requests.length() > 0 or self.des_requests.length() > 0):

            while (selector.length() > 0):
                while (selector.array[0] > self.current):
                    self.move_up()
                while (selector.array[0] < self.current):
                    self.move_down()

                selector.remove()
                self.open_doors()

            if (selector == self.asc_requests):
                selector = self.des_requests
                self.direction = Direction.Descending
            else:
                selector = self.asc_requests
                self.direction = Direction.Ascending

        self.direction = Direction.Stationary

    def move_up(self):
        self.current += 1
        print "Elevator now on floor " + str(self.current) + "."

    def move_down(self):
        self.current -= 1
        print "Elevator now on floor " + str(self.current) + "."

    def open_doors(self):
        print "Elevator opened doors on floor " + str(self.current) + "."

    def run(self):
        while 1:
            self.move()

    def start(self):
        thread = Thread(target = self.run, args = {})
        thread.daemon = True
        thread.start()






