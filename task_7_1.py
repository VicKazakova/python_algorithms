# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в
# виде функции. По возможности доработайте алгоритм (сделайте его умнее).
import random


def bubble_sort(array_second):
    n = 1
    while n < len(array_second):
        for i in range(len(array_second) - n):
            if array_second[i] > array_second[i + 1]:
                array_second[i], array_second[i + 1] = array_second[i + 1], array_second[i]
        n += 1
    return array_second


array_first = []
num = 15  # кол-во элементов в массиве
for _ in range(num):
    a = random.randint(-100, 100)
    array_first.append(a)
print(f'До сортировки: {array_first}')
print(f'После сортировки: {bubble_sort(array_first)}')
