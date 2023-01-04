class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passenger = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passenger.append(name)
        return  True

    def open_seats(self):
        return self.capacity - len(self.passenger)

seats=int( input("Enter fligt capacity: "))
flight = Flight(seats)



for i in range(seats+1):
    person = input("add paassenger name")

    if flight.add_passenger(person):
        print(f"Added{person} to flight succesfully")
    else:
        print(f"NO seat available for{person}")

