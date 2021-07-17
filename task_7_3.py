# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным
# образом. Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: в одной
# находятся элементы, которые меньше медианы, в другой – больше медианы. Задачу можно решить без сортировки
# исходного массива. Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках
import random
m = random.randint(1, 10)
n = 2 * m + 1
the_array = []
for _ in range(n):
    a = (random.randint(0, 100))
    the_array.append(a)
print(the_array)
check_num = n // 2
for i in range(len(the_array)):
    more = [a for a in the_array if a > the_array[i]]
    less = [a for a in the_array if a < the_array[i]]
    if len(more) == check_num and len(less) == check_num:
        print(f'Медиана: {the_array[i]}')
