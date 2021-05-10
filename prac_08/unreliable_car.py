from prac_08.car import Car
import random


class UnreliableCar(Car):
    def __init__(self, name, fuel,reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        num = random.uniform(0,100)
        if num < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = super().drive(0)
        return distance_driven
