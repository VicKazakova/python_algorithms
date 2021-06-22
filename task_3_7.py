# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба
# являться минимальными), так и различаться.
import random
arr = []


def arr_removal():
    num_min = min(arr)
    arr.remove(num_min)
    print(f'{num_min = }')


n = 15  # кол-во элементов в массиве
for _ in range(n):
    i = random.randint(1, 100)
    arr.append(i)
print(f'{arr = }')

arr_removal()
arr_removal()
