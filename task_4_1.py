# 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых
# трех уроков. Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

# 2_4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с
# клавиатуры.
import timeit


def first_var():
    n = int(input('Введите количество элементов: '))
    i = 0
    number = 1
    total_sum = 0
    while i < n:
        total_sum += number
        number = number * (-0.5)
        i += 1
    print(f'Сумма {n} элементов равна: {total_sum}')


def second_var():
    n = int(input('Введите количество элементов: '))
    # i = 0
    # number = 1
    # total_sum = 0

    def recursion(n_f, i_f, number_f, total_sum_f):
        if i_f == n_f:
            return f'Сумма {n} элементов равна: {total_sum_f}'
        elif i_f < n_f:
            return recursion(n_f - 1, i_f, number_f * (-0.5), total_sum_f + number_f)


# print(recursion(n, i, number, total_sum))

time_track1 = (timeit.timeit('first_var()', setup='from __main__ import first_var', number=1))
time_track2 = (timeit.timeit('second_var()', setup='from __main__ import second_var', number=1))
print(f'Без рекурсии: {time_track1}')
print(f'С рекурсией: {time_track2}')
if time_track1 < time_track2:
    print(f'Вариант без рекурсии быстрее в {time_track2 / time_track1} раз')
else:
    print(f'Вариант c рекурсией быстрее в {time_track1 / time_track2} раз')

'''При вводе тестовых значений (1000, 5000, 10000 и т.д. элементов) в данном случае всегда получается, 
что вариант с рекурсией быстрее примерно в 1.5 - 2 раза'''
