#!/user/bin/python3.11         2.2 Свойства property. Декоратор @property
# -*- coding: utf-8 -*-

# link https://proproprogs.ru/python_oop/svoystva-property-dekorator-property


# Посмотрим на более удобный способ работы с приватными атрибутами 
# через специальный объект property, который переводится как свойство. 
# О чем здесь речь? Давайте представим, что мы разрабатываем класс для 
# хранения и обработки данных о персонале:

class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

# И для простоты, в нем будут сохраняться имя и возраст сотрудника в 
# виде приватных атрибутов __name и __old. Разумеется, чтобы обращаться 
# к таким закрытым данным, необходимы сеттеры и геттеры. Пропишем их 
# для возраста:

    def get_old(self):
        return self.__old
 
    def set_old(self, old):
        self.__old = old


# Итак, теперь можно создать экземпляр этого класса:

p = Person('Сергей', 20)

# и через геттер и сеттер считывать и менять возраст сотрудника:

p.set_old(35)
print(p.get_old())      # видим   35

# Это все мы уже умеем и знаем. Но здесь есть одна маленькая проблема. 
# Нам нужно прописывать разные сеттеры и геттеры для разных приватных 
# атрибутов экземпляров класса. Например, добавить еще два для имени. 
# В результате, пользователю этого класса (программисту) придется 
# запоминать и держать в голове названия имен всех этих сеттеров и 
# геттеров. Как можно было бы упростить работу с таким классом? 

# Один из способов – воспользоваться объектом property. 
# Давайте посмотрим на конкретном нашем примере, как это можно сделать.

# В самом классе Person мы пропишем атрибут и придумаем ему имя, 
# допустим, old. Этот атрибут класса будет ссылаться на объект 
# property, которому мы передадим ссылку на геттер и сеттер:

class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old
        
    def get_old(self):
        return self.__old
 
    def set_old(self, old):
        self.__old = old

    old = property(get_old, set_old)

p = Person('Сергей', 20)
a = p.old   
print(a)                    # увидим    20

# Что у нас тут с вами получилось? Из каждого экземпляра класса мы
# совершенно спокойно можем обращаться к атрибуту класса old. 
# Этот атрибут является объектом property. Данный объект так устроен, 
# что при считывании данных он вызывает первый (из перечисленных) 
# метод get_old, этот метод возвращает значение приватного локального
# свойства __old экземпляра класса (p) и именно это значение 
# дальше возвращается атрибутом old. Поэтому переменная (a) будет
# ссылаться на значение текущего возраста сотрудника.

# Если же мы обращаемся к атрибуту класса old и присваиваем ему 
# какое-то значение:

p.old = 35
print(p.old)        # увидим   35

# то автоматически вызывается второй метод set_old и в локальное 
# свойство __old заносится значение, указанное после оператора 
# присваивания. В итоге, в текущем объекте p меняется локальное 
# свойство __old на новое.

# Здесь у вас может возникнуть резонный вопрос, почему строчка:

p.old = 35

print(p.old, p.__dict__)  # увидим   35 {'_Person__name': 'Сергей', '_Person__old': 35}

# не создает новое локальное свойство внутри объекта (p), как это у нас 
# было ранее в программах, а обращается именно к атрибуту класса Person?
# Все дело в приоритете. Если в классе задан атрибут как 
# объект-свойство, то в первую очередь выбирается оно, даже если в 
# экземпляре класса есть локальное свойство с таким же именем. В этом 
# легко убедиться. Давайте создадим свойство с именем old прямо в 
# объекте p через словарь __dict__:

p.__dict__['old'] = 'old in object p'

# затем выведем всю информацию в консоль:

print(p.old, p.__dict__)  # увидим   35 {'_Person__name': 'Сергей', '_Person__old': 35, 'old': 'old in object p'}

# Отображается значение 35, а не строка, то есть, было обращение именно 
# к объекту-свойству old класса Person. А если свойству old в классе 
# присвоить, какое-либо числовое значение, например, 4 (тоесть уже
# не объектом property) то будет отображена строка из объекта p.
# Здесь уже сработают знакомые нам приоритеты: сначала локальная 
# область видимости объекта, затем, класса. Вот этот момент нужно
# хорошо знать, при работе с объектами-свойствами.

# Итак, теперь у нас есть класс и мы можем менять приватное 
# свойство __old экземпляров этого класса через единый 
# атрибут old (считывать информацию и записывать). Это гораздо удобнее 
# использования сеттеров и геттеров. Здесь всего один атрибут и через 
# него естественным образом происходит взаимодействие с закрытым 
# свойством __old.

# Декоратор @property

# Я, думаю, из этого примера вы хорошо поняли, как создается объект 
# property и для чего он нужен. Однако, в нашей реализации есть некое 
# функциональное дублирование: мы можем работать с приватным 
# свойством __old и через сеттер/геттер и через свойство класса old. 
# Конечно, это не критичный момент и на него можно не обращать внимания. 
# Но, было бы лучше, если бы у нас был один интерфейс взаимодействия со 
# свойством __old. Как это можно сделать?

# Смотрите, вот этот класс property позволяет нам на уровне его 
# объектов, использовать функции-декораторы. Если в консоли прописать:

a = property()

# то через ссылку (a) нам будут доступны эти самые функции:

    a.getter() – декоратор для сеттера;
    a.setter() – декоратор для геттера;
    a.deleter() – декоратор для делитера. 

# Что такое декораторы вы должны уже знать, мы с вами об этом говорили 
# в базовом курсе по Python. Ссылка на этот урок будет под этим видео. 
# В двух словах, декоратор – это функция, которая расширяет функционал 
# другой функции. То есть, вот эту строчку:

old = property(get_old, set_old)

# можно переписать и так:

    old = property()
    old = old.setter(set_old)
    old = old.getter(get_old)

# Это будет одно и то же. При вызове метода setter осуществляется 
# встраиванием метода set_old в алгоритм работы объекта property. 
# И то же самое делает метод getter только для геттера. В обоих случаях 
# они возвращают ссылку на объект property, который мы должны сохранять.

# Так вот, мы можем использовать эти декораторы, чтобы сразу нужный нам 
# метод класса превратить в объект-свойство property. Делается это 
# очень просто. Перед геттером (обратите внимание, именно перед 
# геттером, а не сеттером или делитером) прописывается декоратор:

    @property
    def get_old(self):
        return self.__old

# По идее, он теперь представляет объект-свойство с именем get_old:

print(p.get_old)

Но пока присваивание не работает:

p.get_old = 35

# так как мы не прописали декоратор для сеттера. Делается это просто. 
# Метод set_old нужно переименовать в get_old, чтобы имена совпадали 
# (это обязательное условие) и перед ним прописать декоратор:

    @get_old.setter
    def get_old(self, old):
        self.__old = old

# Все, мы сформировали новый объект-свойство с именем get_old. 
# Давайте его переименуем просто в old, а строчки ниже удалим, 
# получим следующий класс Person:

class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old
 
    @property
    def old(self):
        return self.__old
 
    @old.setter
    def old(self, old):
        self.__old = old

# То, что мы сделали, эквивалентно предыдущему варианту с тем лишь 
# отличием, что теперь напрямую вызывать сеттер или геттер для 
# локального свойства __old не получится. У нас остался один интерфейс 
# взаимодействия – объект-свойство old. Именно так чаще всего делают 
# на практике.

# В заключение этого занятия добавлю еще один метод делитер, который 
# вызывается при удалении свойства:

    @old.deleter
    def old(self):
        del self.__old

# Теперь, если выполнить команду:

del p.old
print(p.__dict__)   # увидим   {'_Person__name': 'Сергей'}

# то сработает делитер и мы увидим, что локальное свойство __old было 
# удалено. Конечно, его легко снова создать, достаточно выполнить 
# присвоение, то есть, вызвать сеттер:

p.old = 10

# Вот так гибко можно работать с приватными (закрытыми) локальными 
# свойствами через объект-свойство property. Надеюсь, из этого занятия 
# вы узнали, что это такое, зачем надо и как формировать свои 
# объекты-свойства или через класс property или через декораторы. 

