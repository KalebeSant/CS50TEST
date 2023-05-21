class flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passagengers = []

    def add_passagenger(self, name):
        if not self.open_seats():
            return False    
        self.passagengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passagengers)
flight = flight(3)

people = ["harry", "ron", "hermaione", "ginny" ]
for person in people:
    success = flight.add_passagenger(person)
    if success:
        print(f"added {person} to flight sucessfully")
    else:
        print(f"No avaliable seats for {person}")