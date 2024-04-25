#!/user/bin/python3.11
# -*- coding: utf-8 -*-

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


