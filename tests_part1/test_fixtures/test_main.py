# Использование фикстур.
#
# Допустим, для использования функции summer
# в вашей программе нет подходящих переменных.
# И для подготовки к проведению соответствующего теста требуется выполнить ряд 
# последовательных действий.
# Например в Вашем списке, который представлен
# переменной test_list имеются строковые переменные:
# test_list = [15, '45', 61]
#
# соответвенно при передаче в функцию summer они вызовут сообщение об ошибке.
#
# Здесь Вам необходимо написать фикстуру list_creater которая подготовит для Вас
# данные и переведет все переменные, содержащиеся в test_list в формат Integer
#
import os

import pytest

test_list = [25, '16', '31', 9, 7, 6, '21', 13, 5,
             1, '1', '1', 1, 1, 1, '2', 4, 5,
             27, '4', '5', 9, 7, 6, '17', 13, 5,
             6, '16', '3', 4, 9, 5, '21', 2, 5,
             25, '8', '15', 9, 7, 0, '2', 13, 5]

def summer(*args):
    for arg in args:
        if not isinstance(arg, int):
            return "ОШИБКА"
    if len(args) == 1:
        return "Мало аргументов"
    if sum(args) > 1500:
        return "Большое число"
    return sum(args)


@pytest.fixture
def list_creator():
    for index in range(len(test_list)):
        test_list[index] = int(test_list[index])
    return test_list

# Не меняйте код ниже. Для запуска теста запустите текущий модуль,
# и если он завершиться без ошибок, то задание решено верно!

def test_sum_numbers(list_creator):
    list_sum = sum(list_creator)
    assert summer(*list_creator) == list_sum

if __name__ == "__main__":
    os.system("pytest")