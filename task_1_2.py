# Выполнить логические побитовые операции "И", "ИЛИ" и др. над числами 5 и 6. Выполнить над числом 5 побитовый сдвиг
# вправо и влево на два знака.
a = 5
b = 6
# Логические побитовые операции
# Побитовое И
bit_and = a & b
print(f'Побитовое «И» для {bin(a)} и {bin(b)}: {bin(bit_and)} ({bit_and})')
# Побитовое ИЛИ
bit_or = a | b
print(f'Побитовое «ИЛИ» (OR) для {bin(a)} и {bin(b)}: {bin(bit_or)} ({bit_or})')
# Побитовое НЕ
bit_not_a = ~a
bit_not_b = ~b
print(f'Побитовое отрицание (NOT) для {bin(a)}: {bin(bit_not_a)} ({bit_not_a}), '
      f'для {bin(b)}: {bin(bit_not_b)} ({bit_not_b})')
# Побитовое исключающее ИЛИ
bit_xor = a ^ b
print(f'Исключающее «ИЛИ» (XOR) для {bin(a)} и {bin(b)}: {bin(bit_xor)} ({bit_xor})')
# Побитовые сдвиги
# сдвиг влево
bit_shift_left = a << 2
print(f'Побитовый сдвиг влево для {bin(a)}: {bin(bit_shift_left)} ({bit_shift_left})')
# сдвиг вправо
bit_shift_right = a >> 2
print(f'Побитовый сдвиг вправо для {bin(a)}: {bin(bit_shift_right)} ({bit_shift_right})')
