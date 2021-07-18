# 1. Определение количества различных подстрок с использованием хэш-функции.
import hashlib


def search_strings(s):
    n = len(s)
    arr_str = set()
    for i in range(1, n):
        for j in range(n - i + 1):
            k = hashlib.sha1(s[j:j+i].encode('utf-8')).hexdigest()
            if k not in arr_str:
                arr_str.add(k)
    return len(arr_str)


the_string = 'Пожалуйста проверьте дз сколько можно уже...'
print(f'Количество подстрок: {search_strings(the_string)}')
