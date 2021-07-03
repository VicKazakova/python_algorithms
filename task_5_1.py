# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных
# числа) для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий) и
# вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий,
# чья прибыль ниже среднего.
import collections
less_average = collections.deque()
more_average = collections.deque()

number = int(input('Введите кол-во предприятий: '))
firm_list = []
for m in range(number):
    i = input(f'Введите название предприятия {m + 1}: ')
    firm_list.append(i)
firm_dict = {firm_list[i]: [float(input(f'Введите данные для предприятия {firm_list[i]}. '
                                        f'Квартал {q + 1}: '))
                            for q in range(4)] for i in range(len(firm_list))}
all_profits = [(sum(profits)) for _, profits in firm_dict.items()]
avr_profit = sum(all_profits) / number
firm_profit = list(zip(firm_dict, all_profits))
for firm in firm_profit:
    if firm[1] < avr_profit:
        less_average.append(firm[0])
    elif firm[1] > avr_profit:
        more_average.append(firm[0])
    else:
        pass
print('*' * 20)
print(f'Средняя прибыль для {number} предприятий за год равна: {avr_profit}')
print(f'Прибыль ниже среднего у следующих фирм: {list(less_average)}')
print(f'Прибыль выше среднего у следующих фирм: {list(more_average)}')
