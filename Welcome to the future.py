#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math #импорт пакета math
import numpy #импорт пакета numpy
import matplotlib.pyplot as mpp #импорт пакета matplotlib

# Эта программа рисует график функции, заданной выражением ниже

if __name__=='__main__': #main function
    arguments = numpy.arange(0, 200, 0.1) #возвращает одномерный массив с равномерно разнесенными значениями внутри заданного интервала
    mpp.plot( #функция для отображения графика
        arguments,
        [math.cos(a) * math.cos(a/20.0) for a in arguments] 
    )
    mpp.show()#показать график
