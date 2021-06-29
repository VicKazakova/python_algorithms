# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random
arr = []
n = 5  # кол-во элементов в массиве
for _ in range(n):
    i = random.randint(1, 100)
    arr.append(i)
print(f'{arr = }')
max_arr = max(arr)
min_arr = min(arr)
max_i = arr.index(max_arr)
min_i = arr.index(min_arr)
arr[max_i] = min_arr
arr[min_i] = max_arr
print(f'{arr = }')
