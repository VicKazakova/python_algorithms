# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’,
# ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’,
# ‘E’].
import collections


def from_hex_to_dex(n_hex):
    n_dex = 0
    num = collections.deque(n_hex)
    num.reverse()
    for i in range(len(num)):
        n_dex += dex_list[num[i]] * 16 ** i
    return n_dex


def from_dex_to_hex(numb):
    n_hex = collections.deque()
    while numb > 0:
        d = numb % 16
        for i in dex_list:
            if dex_list[i] == d:
                n_hex.append(i)
        numb //= 16
    n_hex.reverse()
    return list(n_hex)


hex_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
dex_list = collections.defaultdict(int)
final = 0
for i in hex_list:
    dex_list[i] += final
    final += 1


n1 = from_hex_to_dex(input('Введите первое число в шестнадцатиричном формате:\n ').upper())
n2 = from_hex_to_dex(input('Введите второе число в шестнадцатиричном формате:\n ').upper())

print(f'Сумма чисел: {from_dex_to_hex(n1 + n2)}')
print(f'Произведение чисел: {from_dex_to_hex(n1 * n2)}')
