from random import randint
import time

# Ввод имен играющих
igrok1 = input('Введите имя 1-го играющего ')
igrok2 = input('Введите имя 2-го играющего ')
s1 = 0
s2 = 0
for i in range(5):
    print('Партия №', i+1)
    # Моделирование бросания кубика первым играющим
    print('Кубик бросает', igrok1)
    time.sleep(1)
    n1 = randint(1, 6)
    s1 += n1
    print('Выпало:', n1)
    # Моделирование бросания кубика вторым играющим
    print('Кубик бросает', igrok2)
    time.sleep(1)
    n2 = randint(1, 6)
    s2 += n2
    print('Выпало:', n2)
print('Результаты игры. У игрока ', igrok1, ' - ', s1, '. У игрока ', igrok2, ' - ', s2, '.')
if s1 > s2:
    print('Выиграл', igrok1)
elif s1 < s2:
    print('Выиграл', igrok2)
else:
    print('Ничья')
