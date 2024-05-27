from scipy.integrate import quad
import math
import numpy as np
import warnings

warnings.simplefilter("ignore")

def ctg(x):
    return 1 / math.tan(x)


def integrate_function(func, a, b):
    """
    Вычисляет определенный интеграл функции `func` на интервале [a, b].

    :param func: Функция для интегрирования.
    :param a: Нижний предел интегрирования.
    :param b: Верхний предел интегрирования.
    :return: Значение определенного интеграла или сообщение об ошибке.
    """
    try:
        # Проверка на наличие вертикальных асимптот
        if has_poles(func, a, b):
            return "Функция имеет вертикальные асимптоты на интервале интегрирования."

        integral, error = quad(func, a, b)
        return integral
    except Exception as e:
        return str(e)


def has_poles(func, a, b, num_points=1000):
    """
    Проверяет, есть ли у функции вертикальные асимптоты на интервале [a, b].

    :param func: Функция для проверки.
    :param a: Нижний предел интервала.
    :param b: Верхний предел интервала.
    :param num_points: Количество точек для проверки.
    :return: True, если асимптоты обнаружены, иначе False.
    """
    x_vals = np.linspace(a, b, num_points)
    for x in x_vals:
        try:
            if np.isinf(func(x)) or np.isnan(func(x)):
                return True
        except ZeroDivisionError:
            return True
    return False


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
            user_input = user_input.replace('log', 'math.log').replace('ln', 'math.log').replace('exp', 'math.exp').replace('sqrt', 'math.sqrt')
            func = eval("lambda x: " + user_input)
            # Пробное вычисление для проверки корректности функции
            func(10)
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
    print(f"Интеграл функции от {a} до {b} равен {round(result, 2)}")
else:
    print(f"Ошибка при вычислении интеграла: {result}")
