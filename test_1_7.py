#!/user/bin/python3.11
# -*- coding: utf-8 -*-

class Factory:
    @staticmethod
    def build_sequence():
        return list()

    @staticmethod
    def build_number(text):
        return int(text)


class Loader:
    @staticmethod
    def parse_format(string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


res_1 = Loader.parse_format("4, 5, -6", Factory)
res_2 = Loader.parse_format("1, 2, 3, -5, 10", Factory)

print(res_1)
print(res_2)
