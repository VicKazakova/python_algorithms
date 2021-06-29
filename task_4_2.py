# 2. Написать два алгоритма нахождения i-го по счёту простого числа. Без использования «Решета Эратосфена»; Используя
# алгоритм «Решето Эратосфена».
import timeit


def first_var():
    i = int(input('Без решета: Введите число i: '))
    n = i * 100
    lst = [2]
    for m in range(3, n + 1, 2):
        if (m > 10) and (m % 10 == 5):
            continue
        for j in lst:
            if j * j - 1 > m:
                lst.append(m)
                break
            if m % j == 0:
                break
        else:
            lst.append(m)
    print(lst[i - 1])


def second_var():
    i = int(input('С решетом: Введите число i: '))
    n = i * 100
    a = [0] * n
    for z in range(n):
        a[z] = z
    a[1] = 0

    m = 2
    while m < n:
        if a[m] != 0:
            j = m * 2
            while j < n:
                a[j] = 0
                j = j + m
        m += 1
    b = []
    for z in a:
        if a[z] != 0:
            b.append(a[z])
    del a
    print(b[i - 1])


time_track1 = (timeit.timeit('first_var()', setup='from __main__ import first_var', number=1))
time_track2 = (timeit.timeit('second_var()', setup='from __main__ import second_var', number=1))
print(f'Без решета Эратосфена: {time_track1}')
print(f'С использованием решета Эратосфена: {time_track2}')
if time_track1 < time_track2:
    print(f'Вариант без использования решета Эратосфена быстрее в {time_track2 / time_track1} раз')
else:
    print(f'Вариант c использованием решета Эратосфена быстрее в {time_track1 / time_track2} раз')

'''При вводе тестовых значений (1000, 5000, 10000 и т.д. элементов) в данном случае всегда получается, 
что вариант с использованием решета Эратосфена быстрее примерно в 1.0 - 2.1 раза'''
