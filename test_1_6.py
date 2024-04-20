#!/user/bin/python3.11
# -*- coding: utf-8 -*-

class AbstractClass():
    def __new__(cls, *args, **kwargs):
        return "Ошибка: нельзя создавать " \
               "объекты абстрактного класса"


# obj = AbstractClass()
# print(obj)



