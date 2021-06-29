# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами
# минимальный и максимальный элементы в сумму не включать.
import random
arr = []
n = 20  # кол-во элементов в массиве
for _ in range(n):
    i = random.randint(1, 100)
    arr.append(i)
print(f'{arr = }')
max_arr = max(arr)
min_arr = min(arr)
print(f'{max_arr = }')
print(f'{min_arr = }')
max_i = (arr.index(max_arr))
min_i = (arr.index(min_arr))
print(f'{max_i = }')
print(f'{min_i = }')
final_sum = 0
if max_i > min_i:
    arr_slice = arr[min_i + 1:max_i]
    print(arr_slice)
else:
    arr_slice = arr[max_i + 1:min_i]
    print(arr_slice)
print(f'{sum(arr_slice) = }')
