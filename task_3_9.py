# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
from random import random

M = 5
N = 4
a = []
for i in range(N):
    b = []
    for j in range(M):
        b.append(int(random() * 100))
        print(b[j], end='  ')
    a.append(b)
    print('   ')

for i in range(M):
    print("  ", end='  ')
print()
arr2 = []
for i in range(M):
    arr = []
    for j in range(N):
        arr.append(a[j][i])
    arr2.append(min(arr))
max_among_min = max(arr2)
print(f'{max_among_min = }')
