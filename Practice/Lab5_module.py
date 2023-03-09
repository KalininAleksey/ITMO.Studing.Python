from random import randint
import time


def inputName(n):
    print('Введите имя ', n ,' игрока:')
    name = input()
    return name


def game(igrok1, igrok2):
    s1 = 0
    s2 = 0
    for i in range(5):
        print('Партия №', i + 1)
        print('Кубик бросает', igrok1)
        time.sleep(1)
        n1 = randint(1, 6)
        s1 += n1
        print('Выпало:', n1)
        print('Кубик бросает', igrok2)
        time.sleep(1)
        n2 = randint(1, 6)
        s2 += n2
        print('Выпало:', n2)
        scores = [s1, s2]
    return scores


def gameResults(igrok1, igrok2, scores):
    print('Результаты игры. У игрока ', igrok1, ' - ', scores[0], '. У игрока ', igrok2, ' - ', scores[1], '.')
    if scores[0] > scores[1]:
        print('Выиграл', igrok1)
    elif scores[0] < scores[1]:
        print('Выиграл', igrok2)
    else:
        print('Ничья')
