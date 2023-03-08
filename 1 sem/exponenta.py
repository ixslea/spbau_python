"""
Вычисление экспоненты двумя функциями и вывод полученных значений
"""
import math
import matplotlib.pyplot as plt
import numpy as np

"""Рисование графика"""


def graph(start, end):
    arguments = np.arange(start, end, 0.5)
    plt.plot(  # функция для отображения графика
       arguments,
       [my_exp(a) for a in arguments], label='my_exp()')

    plt.plot(  # функция для отображения графика
       arguments,
       [math.exp(a) for a in arguments], '--r', label='math.exp()')
    plt.legend()
    plt.show()


def my_exp(x_arg):
    """
    Вычисление экспоненты при помощи частичного суммирования
    ряда Тейлора
    """
    exp_res = 0
    for i in range(0, 100):
        exp_res += (x_arg**i)/math.factorial(i)
    return exp_res


help(math.exp)
help(my_exp)

print("Результат, встроенной функции:", math.exp(5))
print("Результат, написанной функции:", my_exp(5))
graph(0, 100)
