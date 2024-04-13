#!/user/bin/python3.11
# -*- coding: utf-8 -*-
import random


class Money:
    def __init__(self, money=0):
        self.money = money


# my_money = Money(100)
# your_money = Money(1000)
# print(my_money.money)
# print(your_money.money)


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


# print(points)
# print(len(points))
# print(points[1].color)
# p1 = Point(10, 20)
# p2 = Point(12, 5, 'red')


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

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        test_li = []
        if type(self.a) in (int, float) and self.a > 0:
            test_li.append(self.a)
        if type(self.b) in (int, float) and self.b > 0:
            test_li.append(self.b)
        if type(self.c) in (int, float) and self.c > 0:
            test_li.append(self.c)
        test_li.sort()
        print(test_li)
        if len(test_li) != 3:
            return 1
        if test_li[-1] >= sum(test_li[0:2]):
            return 2
        return 3


##
# tr = TriangleChecker(1, 1, 2)
# print(tr.is_triangle())
#
# tr = TriangleChecker(2, 2, 2)
# print(tr.is_triangle())
#
# tr = TriangleChecker(1, "1", 2)
# print(tr.is_triangle())
#
# tr = TriangleChecker(-1, "1", 2)
# print(tr.is_triangle())
#
# tr = TriangleChecker(3, 4, 5)
# print(tr.is_triangle())
#
# tr = TriangleChecker('3', 4, 5)
# print(tr.is_triangle())
#
# tr = TriangleChecker(3, 4.4, 5)
# print(tr.is_triangle())
#
# tr = TriangleChecker(3, 0, 5)
# print(tr.is_triangle())


class Graph:

    def __init__(self, data: list, is_show=True):
        self.data = data[:]
        self.is_show = is_show

    def set_data(self, data: list):
        self.data = data

    def show_table(self):
        if self.is_show:
            return " ".join(map(str, self.data))
        return "Отображение данных закрыто"

    def show_graph(self):
        if self.is_show:
            return "Графическое отображение данных :" + self.show_table()
        return "Отображение данных закрыто"

    def show_bar(self):
        if self.is_show:
            return "Столбчатая диаграмма: " + self.show_table()
        return "Отображение данных закрыто"

    def set_show(self, fl_show: bool):
        self.is_show = fl_show


# data_graph = list(map(int, input().split()))
#
# d = [1, 2, 3, 4, 5, 6, 10, 28]
#
# gr = Graph(data_graph)
# print(gr.show_bar())
#
# gr.set_show(False)
# print(gr.show_table())
#
# gr1 = Graph(d)
# print(gr1.show_bar())
#
# gr1.set_show(False)
# print(gr1.show_table())
#
# gr2 = Graph(data_graph)
# print(gr2.show_bar())
#
# gr2.set_show(False)
# print(gr2.show_table())
#
# print(id(gr.data))
# print(id(gr1.data))
# print(id(gr2.data))

class CPU:
    def __init__(self, name, fr):
        """
            name - наименование,
            fr -тактовая частота
        """
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name, volume):
        """
            name - наименование;
            volume - объем памяти
        """
        self.name = name
        self.volume = volume


class MotherBoard:

    def __init__(self, name, cpu: CPU, *mem_slots: Memory, total_mem_slots=4,):
        """
            total_mem_slots = 4 - общее число слотов
                памяти (атрибут прописывается с этим
                значением и не меняется);
            name - наименование;
            cpu - ссылка на объект класса CPU;
            mem_slots - список из объектов класса Memory(максимум
            total_mem_slots = 4 штук по максимальному числу
                слотов памяти).
        """
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = total_mem_slots

        if self.total_mem_slots >= len(mem_slots):
            self.mem_slots = mem_slots
            self.total_mem_slots = len(mem_slots)

    def get_config(self):
        li = [f"Материнская плата: {self.name}",
              f"Центральный процессор: {self.cpu.name}, {self.cpu.fr}",
              f"Слотов памяти: {len(self.mem_slots)}"]
        st = "Память:"
        for el in self.mem_slots:
            st += f"{el.name}-{el.volume};"
        li.append(st[:-1])    # последний символ (;) в строке удоляем
        return li


# cpu_1 = CPU("Централ проц_1", 2700)
# mem_1 = Memory("Память_1", 1)
# mem_2 = Memory("Память_2", 2)
# mem_3 = Memory("Память_3", 3)
# mem_4 = Memory("Память_4", 4)
#
# mb = MotherBoard("Материнка_1", cpu_1, mem_3, mem_4)
# # for i in mb.get_config():
# #     print(i)
#
# print(mb.get_config())

