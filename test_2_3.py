#!/user/bin/python3.11
# -*- coding: utf-8 -*-


class RealValue:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class Point:
    x = RealValue()
    y = RealValue()

    def __init__(self, x, y):
        self.x = x
        self.y = y


pt = Point(1.5, 2.3)
pt.x = 15
pt.__dict__['x'] = 18.0
print(pt.x)
