#!/user/bin/python3.11
# -*- coding: utf-8 -*-
from accessify import private, protected


class Clock:
    __time = 0

    def __init__(self, tm):
        self.set_time(tm)

    def set_time(self, tm):
        if self.__check_time(tm):
            self.__time = tm
        else:
            return "Время не int диапазон [0: 100000]"
        return f"время {tm} задано"

    def get_time(self):
        return self.__time

    @staticmethod
    def __check_time(tm):
        return True if ((type(tm) in (int,)) and
                        0 < tm < 100000) else False


clock = Clock(4530)


# print(clock)
# clock.set_time(3444)
# print(clock.get_time())
# print(clock.set_time("gdfsa"))
# print(clock.get_time())
#
# print(clock.set_time(11111))
# print(clock.get_time())
#
# print(clock.set_time(111111))
# print(clock.get_time())


class Money:
    def __new__(cls, money):
        if cls.__check_money(money):
            return super().__new__(cls)

    def __init__(self, money):
        if self.__check_money(money):
            self.__money = money

    def set_money(self, money):
        '''
        передачи нового значения money для изменения
        приватной __money при условии что метод
        check_money(money) возвращает значение True);
        '''
        if self.__check_money(money):
            self.__money = money
            print("__money изменена")
        else:
            print("money are int, >= 0")

    def get_money(self):
        '''
        для получения текущего объема средств (денег);
        '''
        return self.__money

    def add_money(self, mn: 'Money') -> None:
        if self.__check_money(mn.__money) and type(mn) in (Money, ):
            self.__money += mn.__money

    def check_money(self, money):
        return True if self.__check_money(money) else False

    @classmethod
    def __check_money(cls, money):
        '''
        для проверки корректности объема средств в
        параметре money (возвращает True, если значение
        корректно и False - в противном случае).
        '''
        return True if (type(money) in (int, )
                       and money >= 0) else False


# mn_1 = Money(10)
# print(mn_1.get_money())
# mn_2 = Money(20)
# print(mn_2.get_money())
#
# mn_1.set_money(100)
# print(mn_1.get_money())
# mn_2.add_money(mn_1)
# print(mn_2.get_money())
#
# m1 = mn_1.get_money()    # 100
# print(m1)
# m2 = mn_2.get_money()    # 120
# print(m2)

