from flight import Flight
from entities import *
import backend

def fillCustomers():
    src = "resources//customers.json"
    with open(src, "r") as f:
        for line in f:
            print(line)
            cust = Customer(line)
            backend.add(cust)

def fillFlights():
    src = "resources//flights.json"
    with open(src, "r") as f:
        for line in f:
            print(line)
            cust = Flight(line)
            backend.add(cust)

def fillHotels():
    src = "resources//hotels.json"
    with open(src, "r") as f:
        for line in f:
            print(line)
            cust = Hotel(line)
            backend.add(cust)

def fillBus():
    src = "resources//bus.json"
    with open(src, "r") as f:
        for line in f:
            print(line)
            cust = Bus(line)
            backend.add(cust)


if __name__ == "__main__":
    fillCustomers()
    fillFlights()
    fillHotels()
    fillBus()