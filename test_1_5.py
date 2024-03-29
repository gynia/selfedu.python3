#!/user/bin/python3.11
# -*- coding: utf-8 -*-
import random

class Money:
    def __init__(self, money=0):
        self.money = money


my_money = Money(100)
your_money = Money(1000)
print(my_money.money)
print(your_money.money)


class Point:
    def __init__(self, x, y, color="black"):
        self.x = x
        self.y = y
        self.color = color


points = []
for i in range(1, 2000, 2):
    p = Point(i, i)
    points.append(p)
    if i == 3:
        p.color = "yellow"

print(points)
print(len(points))
print(points[1].color)
p1 = Point(10, 20)
p2 = Point(12, 5, 'red')


class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


elements = []
for i in range(217):
    g = None
    rand = random.choice([1, 2, 3])
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    c = random.randint(0, 10)
    d = random.randint(0, 10)
    if rand == 1:
        g = Line(0, 0, 0, 0)
    elif rand == 2:
        g = Rect(a, b, c, d)
    elif rand == 3:
        g = Ellipse(a, b, c, d)
    elements.append(g)


# print(elements)
# print(len(elements))
#
# for i in elements:
#     if isinstance(i, Line):
#         print(type(i))
#         print(i.ep, i.sp)
#


class TriangleChecker:
    def __init__(self):
        pass



tr = TriangleChecker(a, b, c)
