# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
letter = int(input('Введите номер буквы: '))
letter_list = [chr(i) for i in range(ord('a'), ord('z') + 1)]
if letter <= len(letter_list):
    print(f'Под номером {letter} находится буква: {letter_list[letter - 1]}')
else:
    print(f'Ваше число превышает количество букв в алфавите')
