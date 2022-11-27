"""
 Пользователь вводит строку из нескольких слов, разделённых пробелами.
 Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
 Если в слово длинное, выводить только первые 10 букв в слове.
"""
user_string = input("введите предложение ")
words = []
number = 1
for element in range(user_string.count(' ') + 1):
    words = user_string.split()
    if len(str(words)) <= 10:
        print(f" {number}. {words[element]}")
        number += 1
    else:
        print(f" {number}. {words[element][0:10]}")
        number += 1
