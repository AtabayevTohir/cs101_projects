from dataclasses import dataclass,field
from contextlib import contextmanager

class FlightError(Exception):
    pass

@dataclass
class Flight:
    code: str
    destination: str
    distance: int 
    _status: str = field(init=False, default="SCHEDULED")
    
    def __post_init__(self):
        if self.distance < 0:
            raise FlightError(f"Distance for flight {self.code} is invalid")
        
    @property
    def is_long_haul(self):
        return self.distance > 5000

    def __str__(self):
        return f"Flight {self.code} to {self.destination} ({self.distance}km) [{self._status}]"

    def __gt__(self, other):
        return self.distance > other.distance
    
class BoardingChecker:
    def __init__(self,flights, min_dist):
        self.flights = flights
        self.min_dist = min_dist
        self.index = 0
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.flights):
            raise StopIteration

        flight = self.flights[self.index]
        if flight.distance >= self.min_dist:
            flight._status = "CONFIRMED"
        else:
            flight._status = "DELAYED"
        self.index += 1
        return flight
    
def boarding_report(checker):
    confirmed_statuses  = 0
    delayed_statuses = 0
    for flight in checker:
        if flight._status == "CONFIRMED":
            confirmed_statuses += 1
        else:
            delayed_statuses += 1
        yield str(flight)

    yield f"Report: {confirmed_statuses} confirmed, {delayed_statuses} delayed"
        
@contextmanager
def gate_session(name):
    flights = []
    print(f"[BOARD] {name}")
    try:
        yield flights
    except FlightError as e:
        print(f"!!! Error: {e}")
    finally:
        print(f"[GATE] {name} ({len(flights)} flights)")

with gate_session("Morning Departures") as flights:
    flights.append(Flight("AA100", "Paris", 2500))
    flights.append(Flight("BB200", "Tokyo", 5800))
    flights.append(Flight("CC300", "Dublin", 450))

    for line in boarding_report(BoardingChecker(flights, 1000)):
        print(line)

    print(flights[1] > flights[0])

print()

with gate_session("Evening Departures") as flights:
    flights.append(Flight("DD400", "London", -100))

    

 
    