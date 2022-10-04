"""
Вычисление экспоненты двумя функциями и вывод полученных значений
"""
import math


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

print(math.exp((5)))
print(my_exp(5))
