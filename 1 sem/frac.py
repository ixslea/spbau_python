"""
20 фракталов Фибоначчи
"""
import turtle
import math

"""
Функция ниже рисует 20 фракталов Фибоначчи
"""


def fibo_plot(iters, num):
    a_x = 0
    b_x = 1
    x.penup()
    x.setposition(FACTOR, 0)
    x.seth(0)
    x.pensize(3)
    x.pendown()
    x.color("#a6caf0")
    x.left(30*num)
    for i in range(iters):
        fdwd = math.pi * b_x * FACTOR / 2
        fdwd /= 90
        for _ in range(90):
            if i == 0:
                x.forward(fdwd)
            else:
                x.backward(fdwd)
            x.left(1)
        temp = a_x
        a_x = b_x
        b_x = temp + b_x
    x.hideturtle()


FACTOR = 1
ITER = 14

# Fibonacci spiral fractal
for k in range(1, 21):
    x = turtle.Turtle()
    screen = turtle.Screen()
    screen.bgcolor("#faeedd")
    x.speed(10000)
    screen.delay(0)
    fibo_plot(ITER, k)
turtle.done()
