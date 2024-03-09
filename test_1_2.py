#!/user/bin/python3.11
# -*- coding: utf-8 -*-

import pandas as pd
import pyarrow

df = pd.read_csv("product_class.csv")
print(df)


class Goods:
    title = "Мороженое"
    weight = 154
    tp = "Еда"
    price = 1024


Goods.price = 2048
Goods.inflation = 100


class Car:
    pass


setattr(Car, "model", "Тойота")
setattr(Car, "color", "Розовый")
setattr(Car, "number", "П111УУ77")
print(Car.__dict__["color"])


class Notes:
    uid = 1005435
    title = "Шутка"
    author = "И.С. Бах"
    pages = 2


print(getattr(Notes, 'author'))


class Dictionary:
    rus = "Питон"
    eng = "Python"


print(getattr(Dictionary, 'rus_word', False))


class TravelBlog:
    total_blogs = 0


tb1 = TravelBlog()
tb1.name = "Франция"
tb1.days = 6
TravelBlog.total_blogs += 1

tb2 = TravelBlog()
tb2.name = "Италия"
tb2.days = 5
TravelBlog.total_blogs += 1


class Figure:
    type_fig = 'ellipse'
    color = 'red'


fig1 = Figure()
fig1.start_pt = (10, 5)
fig1.end_pt = (100, 20)
fig1.color = 'blue'


del fig1.color

for key in fig1.__dict__:
    print(key, end=" ")
    print()


class Person:
    name = 'Сергей Балакирев'
    job = 'Программист'
    city = 'Москва'


p1 = Person()
p1.job = Person.job
print(True) if "job" in p1.__dict__ else print(False)
print(p1.__dict__)
print(Person.__dict__)



