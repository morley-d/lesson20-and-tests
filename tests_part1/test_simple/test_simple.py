# В этом задании необходимо проверить корректность
# работы функции summer. 
# Вам необходимо написать 4 теста 
# каждый из которых проверил бы правильность
# утверждений.
#
# Изначально функция summer была задумана следующим образом:
#    1.  Функция складывает позиционные аргументы 
#        и возвращает правильный ответ если передано 
#        более двух аргументов.
#        summer(3,6,9) == 18
#       - Реализуйте проверку в функции test_sum()
#    2.  Функция возвращает ответ "Большое число" если
#        сумма переданных аргументов превышает 300.
#        summer(299, 25) == "Большое число"
#        - Реализуйте проверку в функции test_big_number()
#    3.  Функция возвращает ответ "Мало аргументов"
#        Если передан только один аргумент.
#        summer(301) == "Мало аргументов"
#        - Реализуйте проверку в функции test_one_arg
#    4.  Функция возвращает ответ "ОШИБКА"
#        Если в аргументах передано не целое число.
#        summer("qwe") == "ОШИБКА"
#        - Реализуйте проверку в функции test_wrong_arg
#
import os

def summer(*args):
    for arg in args:
        if not isinstance(arg, int):
            return "ОШИБКА"
    if len(args) == 1:
        return "Мало аргументов"
    if sum(args) > 300:
        return "Большое число"
    return sum(args)


def test_sum():
    # TODO Напишите Ваш код здесь
    pass

def test_big_number():
    # TODO Напишите Ваш код здесь
    pass

def test_one_arg():
    # TODO Напишите Ваш код здесь
    pass

def test_wrong_arg():
    # TODO Напишите Ваш код здесь
    pass


# Имитируем команду pytest при запуске модуля
if __name__ == "__main__":
    os.system("pytest")
