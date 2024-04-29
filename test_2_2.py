#!/user/bin/python3.11
# -*- coding: utf-8 -*-

class Car:
    def __init__(self, model=None):
        if self.validate(model) or model is None:
            self.__model = model

    @staticmethod
    def validate(model: str):
        return True if (type(model) in (str,)
                        and 100 >= len(model) >= 2) else False

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if self.validate(model):
            self.__model = model


car = Car()
print(car.model)
print(car.__dict__)
car.model = "Toyota"
print(car.model)
print(car.validate("a"))
print(car.validate(45))
print(car.__dict__)




