"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

words_list = ["разработка", "администрирование", "protocol", "standart"]
bytes_word_list = []
for word in words_list:
    bytes_word_list.append(str.encode(word))

for word in bytes_word_list:
    print(word.decode())
    print(type(word.decode()))
    print(word)
    print(type(word))
