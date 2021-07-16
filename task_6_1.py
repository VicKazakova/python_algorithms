# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех
# уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти. Примечание:
# Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи. Результаты
# анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность вашей ОС.
import sys
import random
'''Python 3.9, 64-разрядная ОС'''


def c_s(x):
    size = sys.getsizeof(x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                size += sys.getsizeof(key)
                size += sys.getsizeof(value)
        elif not isinstance(x, str):
            for item in x:
                size += sys.getsizeof(item)
    return size


# Задача 1
arr1 = []
arr2 = []
n = 5  # кол-во элементов в массиве
for _ in range(n):
    i = random.randint(1, 100)
    arr1.append(i)
    if i % 2 == 0:
        j = arr1.index(i)
        arr2.append(j)
print(f'{arr1 = }')
print(f'{arr2 = }')

print(f'Под переменные из задачи 1 зайдествовано'
      f' {c_s(n) + c_s(arr1) + c_s(arr2) + c_s(i) + c_s(j)} байт памяти')


# Задача 2
m = 5
n = 4
a = []
for i in range(n):
    b = []
    total_sum = 0
    print(f"{i + 1}-я строка:")
    for j in range(m - 1):
        n = int(input())
        total_sum += n
        b.append(n)
    b.append(total_sum)
    a.append(b)

for i in a:
    print(i)

print(f'Под переменные из задачи 2 зайдествовано'
      f' {c_s(n) + c_s(m) + c_s(a) + c_s(i) + c_s(j) + c_s(b) + c_s(total_sum)} байт памяти')

# Задача 3
number = (input('Введите натуральное число: '))
odd = 0
even = 0
for n in number:
    n = int(n)
    if n % 2 == 0:
        even += 1
    else:
        odd += 1
print(f'Четных: {even}, нечетных: {odd}')

print(f'Под переменные из задачи 3 зайдествовано'
      f' {c_s(number) + c_s(odd) + c_s(even) + c_s(n)} байт памяти')
