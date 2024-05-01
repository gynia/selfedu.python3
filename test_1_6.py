#!/user/bin/python3.11
# -*- coding: utf-8 -*-

class AbstractClass():
    def __new__(cls, *args, **kwargs):
        return "Ошибка: нельзя создавать " \
               "объекты абстрактного класса"


# obj = AbstractClass()
# print(obj)


class SingletonFive():
    __instance = None
    count = 0
    is_enumerate = True

    def __new__(cls, *args, **kwargs):
        # print("func __new__")
        if cls.count < 5:
            cls.__instance = super().__new__(cls)
            # print(cls.count)
            cls.count += 1
        else:
            cls.is_enumerate = False
        return cls.__instance

    def __init__(self, *args, **kwargs):
        if self.is_enumerate:
            self.__setattr__("name", *args)
        # print("func __init__")
        # print(self.__dict__)
        # print(self.__instance)
        # print(id(self))

    def __del__(self):
        self.__instance = None
        self.cls_count = 0
        self.is_enumerate = True


objs = [SingletonFive(str(n)) for n in range(10)]


# print(objs)
# print(len(objs))


class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


class Dialog():
    def __new__(cls, *args, **kwargs):
        if TYPE_OS == 1:
            dlg = DialogWindows()
        else:
            dlg = DialogLinux()
        dlg.name = str(*args)
        return dlg


# TYPE_OS = 1    # 1 - Windows; 2 - Linux
# di = Dialog()
# print(di.name)
# print(type(di))
# print(di.__dict__)
#
# dlg_1 = Dialog("name_1")
# print(dlg_1.name)
# print(type(dlg_1))
# print(dlg_1.__dict__)
#
# TYPE_OS = "34"    # 1 - Windows; 2 - Linux
# dlg_2 = Dialog("name_2")
# print(dlg_2.name)
# print(type(dlg_2))
# print(dlg_2.__dict__)
#
# di = Dialog(3)
# print(di.name)
# print(type(di))
# print(di.__dict__)
#
# print(isinstance(dlg_1, DialogWindows))
# print(isinstance(dlg_2, DialogLinux))



