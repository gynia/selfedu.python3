#!/user/bin/python3.11
# -*- coding: utf-8 -*-


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




