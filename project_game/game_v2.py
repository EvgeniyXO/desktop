import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    

    count = 0
    number = np.random.randint(1, 101)
    min = 0
    max = 100
    while True:
        predict_number = round((min+max)/2)
        #predict = int(input())
        count += 1
        if number == predict_number:
            break
        elif number > predict_number:
            min = predict_number
            round((max + min) / 2)
        elif number < predict_number:
            max = predict_number
            (round((max+min)/2))
                
    return(count)

print(f'Количество попыток:{random_predict()}')


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
score_game(random_predict)