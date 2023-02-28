"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""
import subprocess
import chardet

resources = [['ping', 'yandex.ru'], ['ping', 'youtube.com']]

for resource in resources:
    ping = subprocess.Popen(resource, stdout=subprocess.PIPE)
    for line in ping.stdout:
        result = chardet.detect(line)
        line = line.decode(result['encoding']).encode('utf-8')
        print(line.decode('utf-8'))
