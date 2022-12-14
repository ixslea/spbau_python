"""Задание: создать класс, объекты которого могут бесконечно выдавать числа Фибоначчи"""
from math import sqrt

fibs = [] # Лист для хранения чисел Фибоначчи

class Fib:
    """По объектам этого класса можно итерироваться и получать числа Фибоначчи"""

    class _Fib_iter:

        """Внутренний класс — итератор"""
        def __init__(self):
            self.i = 0
            self.fibs = fibs # Подключение листа для чисел Фибоначчи

        def __add__(self, a):
            """Функция, добавляющая в лист элемент"""
            self.fibs.append(a)

        def __next__(self):
            """Функция, вычисляющая числа Фибоначчи и возвращающая их"""
            if self.i >= 20:            # Если хочется остановиться на каком-то числе
                raise StopIteration()
            j = self.i
            self.i += 1
            finding_fib = int((((1+sqrt(5))**j)-((1-sqrt(5)))**j)/(2**j*sqrt(5))) # Формула вычисления числа Фибоначчи
            self.__add__(finding_fib)
            return self.fibs[j]


    def __iter__(self):
        """Создать и вернуть итератор"""
        return Fib._Fib_iter()

f = Fib()

# Вывод
for fib in f:
    print(fib)
