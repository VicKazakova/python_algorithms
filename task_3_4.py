# 4. Определить, какое число в массиве встречается чаще всего.
import random
arr = []
n = 15  # кол-во элементов в массиве
for _ in range(n):
    i = random.randint(1, 20)
    arr.append(i)
print(f'{arr = }')

num = arr[0]
max_frq = 1
for i in range(n - 1):
    frq = 1
    for k in range(i + 1, n):
        if arr[i] == arr[k]:
            frq += 1
    if frq > max_frq:
        max_frq = frq
        num = arr[i]

if max_frq > 1:
    print(max_frq, 'раз(а) встречается число', num)
else:
    print('Все элементы уникальны')
