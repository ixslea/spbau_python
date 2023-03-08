"""Даны матрица А размером N*N, вектор B высотой N. Требуется найти вектор X такой, что AX = B."""

from numpy import array, concatenate
from numpy.linalg import norm
from numpy.linalg import solve as solve_out_of_the_box

a = array([
    [1.5, 2.0, 1.5, 2.0],
    [3.0, 2.0, 4.0, 1.0],
    [1.0, 6.0, 0.0, 4  ],
    [2.0, 1.0, 4.0, 3  ]
], dtype=float)

b = array([5, 6, 7, 8], dtype=float)

'''Решение в векторной форме'''


def vector_gauss(a, b):
    ab = concatenate((a, array([b]).T), axis=1)  # concatenate заодно и скопирует
    d = len(ab)  # размер по старшему измерению

    # прямой ход
    for i in range(d):
        ab[i] = ab[i] / ab[i, i]
        for j in range(i+1, d):
            ab[j] = ab[j] - ab[i] * ab[j, i]

    # обратный ход
    for i in range(d - 1, -1, -1):
        sub = 0
        for j in range(i+1, d):
            sub += ab[j] * ab[i, j]
        ab[i] = ab[i] - sub
    x = ab[:, -1]  # Последний столбец
    return x


solution = vector_gauss(a, b)
oob_solution = solve_out_of_the_box(a, b)


print(solution)
print("Макс отклонение компоненты решения:", norm(solution-oob_solution, ord=1))
