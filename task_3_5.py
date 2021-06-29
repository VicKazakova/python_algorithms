# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
import random
arr = []
arr_min = []
n = 15  # кол-во элементов в массиве
for _ in range(n):
    i = random.randint(-100, 100)
    arr.append(i)
for i in arr:
    if 0 > i:
        arr_min.append(i)
    else:
        pass
min_elem = max(arr_min)
ind_elem = arr_min.index(min_elem)
print(arr_min)
print(f'{min_elem = }, {ind_elem = }')
