# 6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10
# попыток. После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то,
# что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.
import random
number = random.randint(0, 100)
total_count = 10
user_attempts = 1
while user_attempts != total_count:
    print(f'Попытка номер {user_attempts}')
    user_answer = int(input('Я загадал число от 0 до 100. Попробуй отгадать! '))
    if user_answer == number:
        print('Поздравляю! Верно!')
        break
    elif user_answer > number:
        print('Нет. Меньше!')
        user_attempts += 1
    elif user_answer < number:
        print('Нет. Больше!')
        user_attempts += 1
if user_attempts > total_count:
    print(f'Вы проиграли. Я загадал: {number}')
