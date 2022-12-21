from abc import abstractmethod

class Person:
    def __init__(self,FIO):
        self.FIO = FIO

class Driver(Person):
    def __init__(self,FIO,drive_exp):
        self.FIO = FIO
        self.drive_exp = drive_exp

class Engine:
    def __init__(self,power,company):
        self.power = power
        self.company = company


class Car:
    def __init__(self,car_class,brand,weight,driver,engine):
        self.car = car_class
        self.brand = brand
        self.weight = weight
        self.driver = driver
        self.engine = engine

    @staticmethod
    def start():
        print("GO")

    @staticmethod
    def stop():
        print("STOP")

    @staticmethod
    def turn_left():
        print("TURN LEFT")

    @staticmethod
    def turn_right():
        print("TURN RIGHT")

    def __str__(self):
        return(f"Brand of Auto: {self.brand} "
              f"Car class: {self.car} "
              f"Weight: {self.weight}"
              f"Driver: {self.Driver.FIO}"
              f"Engine power: {self.Engine.power}"
              f"Engine company: {self.Engine.company}"
              )

class Lorry:
    def __init__(self, brand, car_class, weight, driver, engine, capacity):
        self.car = car_class
        self.brand = brand
        self.weight = weight
        self.driver = driver
        self.engine = engine
        self.capacity = capacity

    def __str__(self):
        return (f"Brand of Auto: {self.brand} "
              f"Car class: {self.car_class} "
              f"Weight: {self.weight}"
              f"Driver: {self.Driver.FIO}"
              f"Engine power: {self.Engine.power}"
              f"Engine company: {self.Engine.company}"
              f"Load capacity: {self.capacity}")


    







