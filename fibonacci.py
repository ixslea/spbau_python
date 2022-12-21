"""Задание: создать класс, объекты которого могут бесконечно выдавать числа Фибоначчи"""
from math import sqrt
from itertools import islice

class Fib:
    """По объектам этого класса можно итерироваться и получать числа Фибоначчи"""
    class _Fib_iter:
        """Внутренний класс — итератор"""
        def __init__(self):
            self.i = 0

        def __next__(self):
            """Функция, вычисляющая числа Фибоначчи и возвращающая их"""
            j = self.i
            self.i += 1
            finding_fib = int((((1+sqrt(5))**j)-((1-sqrt(5)))**j)/(2**j*sqrt(5)))   # Формула вычисления числа Фибоначчи
            return finding_fib

    def __iter__(self):
        """Создать и вернуть итератор"""
        return Fib._Fib_iter()


f = Fib()

# Вывод
for fib in islice(Fib(), 20):
    print(fib)
