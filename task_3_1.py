# # 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2
# до 9.
def total_count_func(m):
    total_count = 0
    for elem in arr:
        if elem % m == 0:
            total_count += 1
    print(f'Кратно {m}: {total_count} чисел')


arr = []
for i in range(2, 100):
    arr.append(i)
total_count_func(2)
total_count_func(3)
total_count_func(4)
total_count_func(5)
total_count_func(6)
total_count_func(7)
total_count_func(8)
total_count_func(9)
