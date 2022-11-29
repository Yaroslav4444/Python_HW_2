"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор
натуральных чисел.У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент
с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например,
my_list = [7, 5, 3, 3, 2].
"""

rating_list = [7, 5, 3, 3, 2]
print(f"Текущие оценки : {rating_list}")
score = int(input("Введите оценку :"))

for el in range(len(rating_list)):
    if rating_list[el] == score:
        rating_list.insert(el + 1, score)
        break
    elif rating_list[0] < score:
        rating_list.insert(0, score)
    elif rating_list[-1] > score:
        rating_list.append(score)
    elif rating_list[el] > score and rating_list[el + 1] < score:
        rating_list.insert(el + 1, score)
        break

print(f"Итоговые оценки : {rating_list}")
