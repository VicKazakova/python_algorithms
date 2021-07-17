# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
import random


def merge_sort(array, start, end):
    if end - start > 1:
        mid = (start + end) // 2
        merge_sort(array, start, mid)
        merge_sort(array, mid, end)
        merge_list(array, start, mid, end)


def merge_list(array, start, mid, end):
    left = array[start:mid]
    right = array[mid:end]
    k = start
    i = 0
    j = 0
    while start + i < mid and mid + j < end:
        if left[i] <= right[j]:
            array[k] = left[i]
            i = i + 1
        else:
            array[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            array[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            array[k] = right[j]
            j = j + 1
            k = k + 1


the_array = []
num = 15  # кол-во элементов в массиве
for _ in range(num):
    a = round(random.uniform(0, 50), 2)
    the_array.append(a)
print(f'До сортировки: {the_array}')
merge_sort(the_array, 0, len(the_array))
print(f'После сортировки: {the_array}')
