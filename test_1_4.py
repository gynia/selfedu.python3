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
    # data = []
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

# Имеется следующий класс для считывания информации из входного потока:
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


# # Раскоментировать для теста КЛАССА DataBase
# print()
# # программу не менять, только добавить два метода
# lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
# # в формате: id, name, old, salary (записанные через пробел)

class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    # здесь добавлять методы
    def insert(self, data):
        data = [list(str.split(t)) for t in data]
        for lis in data:
            self.lst_data.append({val: lis[key] for key, val in enumerate(self.FIELDS)})

    def select(self, a, b):
        return self.lst_data[a:(b + 1)]


# # Раскоментировать для теста КЛАССА DataBase
# db = DataBase()
# db.insert(lst_in)
# print(db.lst_data)
# print(db.select(0, 10))
# print(db.select(0, 5))
# print(db.select(0, 1))


class Translator:
    def add(self, eng, rus):
        if 'tr' not in self.__dict__:
            self.tr = {}

        self.tr.setdefault(eng, [])
        # здесь продолжайте метод add
        if rus not in self.tr[eng]:
            self.tr[eng].append(rus)

    def remove(self, eng):
        # здесь продолжайте метод remove
        del self.tr[eng]

    def translate(self, eng):
        # здесь продолжайте метод translate
        return self.tr.get(eng)


# здесь создавайте объект класса Translator
print()
tr = Translator()
tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("go", "ходить")
tr.add("milk", "молоко")
print(tr.tr)

tr.remove("go")
print(tr.tr)

print(tr.translate("car"))
print(tr.translate("asdf"))

