"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" исключение,
придумайте как это сделать
"""


class NotBytesException(Exception):
    def __init__(self, *args):
        if args:
            self.error_text = args[0]
        else:
            self.error_text = None

    def __str__(self):
        if self.error_text:
            return f"NotBytesException: {self.error_text}"
        else:
            return "NotBytesException!"


words_list = ["attribute", "класс", "функция", "type"]
byte_words_list = []
for word in words_list:
    try:
        if "\\" in str(bytes(word, "utf-8")):
            raise NotBytesException(f"{word} can not be represented as bytes")
        byte_words_list.append(bytes(word, "utf-8"))
    except NotBytesException as e:
        print(e)

for word in byte_words_list:
    print(type(word))
    print(word)
    print(len(word))
