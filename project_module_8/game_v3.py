"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Сбрасываем счётчик и определяем верхнюю и нижнюю границы поиска
    count = 0
    minimum = 0
    maximum = 101
    predict_number = (maximum + minimum) // 2 #Устанавливаем первое число поиска
    # Запускаем цикл поиска числа
    while predict_number != number:
        
        if predict_number > number:
            maximum = predict_number 
        elif predict_number < number:
            minimum = predict_number
            
        count += 1    
        predict_number = round((maximum + minimum) // 2)            
        
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
