#!/user/bin/python3.11
# -*- coding: utf-8 -*-

class MediaPlayer:
    filename = None

    def open(self, file):
        self.filename = file

    def play(self):
        print(f"Воспроизведение {self.filename}")


media1 = MediaPlayer()
media2 = MediaPlayer()

media1.open("filemedia1")
media2.open("filemedia2")

media1.play()
media2.play()


class Graph:
    #data = []
    LIMIT_Y = [0, 10]

    def set_data(self, data: list):
        self.data = data

    def draw(self):
        for d in self.data:
            if self.LIMIT_Y[1] >= d >= self.LIMIT_Y[0]:
                print(d, end=" ")


li = [10, -5, 100, 20, 0, 80, 45, 2, 5, 7]
graph_1 = Graph()
graph_1.set_data(li)
graph_1.draw()


#Имеется следующий класс для считывания информации из входного потока:
import sys


class StreamData:

    def create(self, FIELDS: tuple, lst_in: list):
        if len(FIELDS) != len(lst_in):
            return False
        for n, Fi in enumerate(FIELDS):
            setattr(self, Fi, lst_in[n])
            if Fi not in self.__dict__:
                return False
        return True


class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


# # Раскоментировать для теста КЛАССА StreamData
# sr = StreamReader()
# data, result = sr.readlines()
# print(result)
# print(data.__dict__)


# программу не менять, только добавить два метода
lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
# в формате: id, name, old, salary (записанные через пробел)


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    # здесь добавлять методы


db = DataBase()
db.insert(lst_in)
