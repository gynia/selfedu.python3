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


# res_1 = Loader.parse_format("4, 5, -6", Factory)
# res_2 = Loader.parse_format("1, 2, 3, -5, 10", Factory)
#
# print(res_1)
# print(res_2)


from string import ascii_lowercase, digits

CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
CHARS_CORRECT = CHARS + CHARS.upper() + digits


class TextInput:
    CHARS_CORRECT = CHARS_CORRECT

    def __init__(self, name, size=10):
        if self.check_name(name):
            self.name = name
            self.size = size
        else:
            raise ValueError("некорректное поле name")

    def get_html(self):
        return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"

    @classmethod
    def check_name(cls, name):
        if 51 > len(name) > 2 and type(name) in (str,):
            for s in name:
                if s in cls.CHARS_CORRECT:
                    return True
        return False


class PasswordInput:
    CHARS_CORRECT = CHARS_CORRECT

    def __init__(self, name, size=10):
        if self.check_name(name) and type(size) == int:
            self.name = name
            self.size = size
        else:
            raise ValueError("некорректное поле name")

    def get_html(self):
        return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"

    @classmethod
    def check_name(cls, name):
        if 51 > len(name) > 2 and type(name) in (str,):
            for s in name:
                if s in cls.CHARS_CORRECT:
                    return True
        return False


class FormLogin:
    """
        Класс для работы с формами ввода логин/пароль
    """

    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


# # эти строчки не менять
# login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
# html = login.render_template()
# print(html)
#
# # name = "Логин a;sd "
# # size = 12
# # login = FormLogin(TextInput(name), PasswordInput(name))
# # html = login.render_template()
# # print(html)
# #
# # name = "Логин a;sd "
# # size = 53
# # login = FormLogin(TextInput(name), PasswordInput(name))
# # html = login.render_template()
# # print(html)
# #
# # name = "Лоghгин a6sd "
# # size = 65
# # login = FormLogin(TextInput(name), PasswordInput(name, size))
# # html = login.render_template()
# # print(html)
# #
# # name = "Лоghгин a@sd "
# # size = "53"
# # login = FormLogin(TextInput(name), PasswordInput(name, size))
# # html = login.render_template()
# # print(html)
# #
# # name = "Лоghгин a6sd "
# # size = "53"
# # login = FormLogin(TextInput(name), PasswordInput(name, size))
# # html = login.render_template()
# # print(html)
# #
# # name = "Лоghгин a6sd "
# # size = 64
# # login = FormLogin(TextInput(name), PasswordInput(name, size))
# # html = login.render_template()
# # print(html)
