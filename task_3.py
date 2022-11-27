"""
 Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому
 времени года относится месяц (зима, весна, лето, осень). Напишите решения
 через list и через dict.
"""
# решение через список:

seasons_list = ["зима за окном", "весна за окном", "лето за окном",
                "осень за окном"]
user_month = int(input("Введите номер месяца года :"))
if user_month in (12, 1, 2):
    print(seasons_list[0])
elif user_month in (3, 4, 5):
    print(seasons_list[1])
elif user_month in (6, 7, 8):
    print(seasons_list[2])
elif user_month in (9, 10, 11):
    print(seasons_list[3])
else:
    print("Дед,ты опять забыл выпить таблетки!!!")

# решение через словарь:

seasons_dict = {1: "зима за окном", 2: "весна за окном", 3: "лето за окном",
                4: "осень за окном"}
user_month = int(input("Введите номер месяца года :"))
if user_month in (12, 1, 2):
    print(seasons_dict.get(1))
elif user_month in (3, 4, 5):
    print(seasons_dict.get(2))
elif user_month in (6, 7, 8):
    print(seasons_dict.get(3))
elif user_month in (9, 10, 11):
    print(seasons_dict.get(4))
else:
    print("Дед,ты опять забыл выпить таблетки!!!")
