# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого
# предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
# предприятий, чья прибыль выше среднего и ниже среднего.
from collections import namedtuple

Enterprise = namedtuple("Enterprise", "Name Quarter1 Quarter2 Quarter3 Quarter4")
enterprises = []
more_average = []
less_average = []
total_average_profit = 0.0
average_dict = {}
add_new = 'y'
while add_new == 'y':
    enterprises.append(Enterprise(input("Введите имя компании: "), int(input("Прибыль за 1 квартал: ")),
                                  int(input("Прибыль за 2 квартал: ")), int(input("Прибыль за 3 квартал: ")),
                                  int(input("Прибыль за 4 квартал: "))))
    add_new = input("Добавить еще компанию? Нажмите [y/n]")
    if add_new.upper() != "Y" and add_new.upper() != "N":
        print("Введено неверное значение. Программа аварийно завершена :)")
        break
    elif add_new.upper() == "N":
        for enterprise in enterprises:
            average_dict[enterprise.Name] = (
                            enterprise.Quarter1 + enterprise.Quarter2 + enterprise.Quarter3 + enterprise.Quarter4) / 4
            total_average_profit += average_dict[enterprise.Name]
        total_average_profit = total_average_profit / len(enterprises)
        print(f"Средняя прибыль за год по всем предприятиям - {total_average_profit:0.2f}")

        for key in average_dict:
            if average_dict[key] >= total_average_profit:
                more_average.append(key)
            else:
                less_average.append(key)
        print(f"Компании, у которых прибыль выше среднего {total_average_profit:0.2f}:")
        for el in more_average:
            print(f"{el} - {average_dict[el]}")
        print(f"Компании, у которых прибыль ниже среднего {total_average_profit:0.2f}:")
        for el in less_average:
            print(f"{el} - {average_dict[el]}")
        break
