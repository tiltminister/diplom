from scipy.integrate import quad
import math


def ctg(x):
    return 1/math.tan(x)

def integrate_function(func, a, b):
    """
    Вычисляет определенный интеграл функции `func` на интервале [a, b].

    :param func: Функция для интегрирования.
    :param a: Нижний предел интегрирования.
    :param b: Верхний предел интегрирования.
    :return: Значение определенного интеграла или сообщение об ошибке.
    """
    try:
        integral, error = quad(func, a, b)
        return integral
    except Exception as e:
        return str(e)


def input_function():
    """
    Получает функцию от пользователя и возвращает её в виде lambda выражения.

    :return: Функция для интегрирования.
    """
    while True:
        try:
            user_input = input("Введите функцию от x (например, sin(x), log(x), exp(x), x**2 + 2*sin(x)):\n")
            # Добавляем 'math.' перед каждой функцией
            user_input = user_input.replace('sin', 'math.sin').replace('cos', 'math.cos').replace('tan', 'math.tan')
            user_input = user_input.replace('log', 'math.log').replace('exp', 'math.exp').replace('sqrt', 'math.sqrt')
            func = eval("lambda x: " + user_input)
            # Пробное вычисление для проверки корректности функции
            func(1)
            return func
        except Exception as e:
            print(f"Ошибка ввода функции: {e}. Пожалуйста, попробуйте снова.")


def input_limits():
    """
    Получает пределы интегрирования от пользователя.

    :return: Нижний и верхний пределы интегрирования.
    """
    while True:
        try:
            a = float(input("Введите нижний предел интегрирования: "))
            b = float(input("Введите верхний предел интегрирования: "))
            return a, b
        except ValueError:
            print("Ошибка ввода. Пожалуйста, введите числовое значение.")


# Получаем функцию и пределы интегрирования от пользователя
func = input_function()
a, b = input_limits()

# Пытаемся вычислить интеграл и выводим результат или сообщение об ошибке
result = integrate_function(func, a, b)
if isinstance(result, float):
    print(f"Интеграл функции от {a} до {b} равен {round(result,2)}")
else:
    print(f"Ошибка при вычислении интеграла: {result}")
