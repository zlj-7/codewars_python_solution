class Dinglemouse(object):

    def __init__(self, queues, capacity):
        self.queues = [list(x) for x in queues]
        self.capacity = capacity

    def theLift(self):
        stops = [0]
        elevator = []

        people_waiting = True

        while people_waiting:
            people_waiting = False

            # Going up
            for floor in range(0, len(self.queues)):
                stop_at_floor = False

                for person in elevator[:]:
                    if person == floor:
                        elevator.remove(person)
                        stop_at_floor = True

                for person in self.queues[floor][:]:
                    if person > floor:
                        stop_at_floor = True
                        if self.capacity > len(elevator):
                            elevator.append(person)
                            self.queues[floor].remove(person)
                        else:
                            people_waiting = True

                if stop_at_floor and not stops[-1] == floor:
                    stops.append(floor)

            # Going down
            for floor in range(len(self.queues) -1, -1, -1):
                stop_at_floor = False

                for person in elevator[:]:
                    if person == floor:
                        elevator.remove(person)
                        stop_at_floor = True

                for person in self.queues[floor][:]:
                    if person < floor:
                        stop_at_floor = True

                        if self.capacity > len(elevator):
                            elevator.append(person)
                            self.queues[floor].remove(person)
                        else:
                            people_waiting = True

                if stop_at_floor and not stops[-1] == floor:
                    stops.append(floor)
        if stops[-1] != 0:
            stops.append(0)

        return stops