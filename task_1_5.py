# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
a = (input('Введите первую букву: '))
b = (input('Введите вторую букву: '))
letter_list = [chr(i) for i in range(ord('a'), ord('z') + 1)]
a_place = letter_list.index(a) + 1
b_place = letter_list.index(b) + 1
print(f'Буква {a} находится в алфавите под номером {a_place}')
print(f'Буква {b} находится в алфавите под номером {b_place}')
distance = 0
if a_place > b_place:
    distance = a_place - b_place - 1
    print(f'Между буквами {distance} букв')
elif a_place < b_place:
    distance = b_place - a_place - 1
    print(f'Между буквами {distance} букв')
else:
    print('Это одна и та же буква')