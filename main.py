# Лабораторная работа №1
# Написать программу, которая читая символы из бесконечной последовательности (эмулируется конечным файлом,
# читающимся поблочно), распознает, преобразует и выводит на экран лексемы по определенному правилу.
# Лексемы разделены пробелами. Преобразование делать по возможности через словарь.
# Для упрощения под выводом числа прописью подразумевается последовательный вывод всех цифр числа.
# Регулярные выражения использовать нельзя.
# Вариант 5.
# Четные натуральные числа, не превышающие 5 цифр. Каждое число на нечетном месте выводить словами.

def is_correct_number(str_num):
    try:
        num = int(str_num)
        if len(str_num) <= 5 and num % 2 == 0 and num > 0:
            return True
        else:
            return False
    except ValueError:
        return False


def transform_number(number):
    nums_to_words = {0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
                     6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
    result = ''
    for digit in number:
        result += f'{nums_to_words[int(digit)]} '
    return result


def read_file(filename, buffer_len):
    with open(filename, 'r') as file:
        buffer = file.read(buffer_len).split()

        if not buffer:
            return print(f'Файл {filename} пустой')

        while buffer:
            for i in range(len(buffer)):
                if is_correct_number(buffer[i]):
                    if (i + 1) % 2 != 0:
                        print(f'{buffer[i]}: {transform_number(buffer[i])}')
                    else:
                        print(buffer[i])

            buffer = file.read(buffer_len).split()


read_file('numbers.txt', 1000)
