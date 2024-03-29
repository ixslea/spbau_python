
"""Импортируем необходимые модули"""
import random 
from math import log
import numpy as np

"""Задаём пределы интегрирования""" 
a = -1
b = 2

"""Кол-во проходов"""
N = 10000 

  
"""Переменная, в которой будет храниться сумма функций при разных x"""
integral = 0.0

  
"""Функция, считающая значение при заданном x"""
def f(x): 
    return ((1+x**2)/(1+x**4))

  

"""Итерирование и суммирование результатов при разных х"""
for i in range(N):
    i = random.uniform(a, b) 
    integral += f(i) 

  

"""Подсчет ответа"""
answer = (b-a)/float(N)*integral 

 
"""Вывод ответа"""
print("Вычисленное значение интеграла с помощью метода Монте-Карло {}.".format(answer)) 
 
