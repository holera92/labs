import random

while True:
    secret = int(random.random() * 101)
    win = False

    print("{Приветственное сообщение от игры}")

    for i in range(5):
        guess = int(input())
        if guess > secret:
            print("Загаданное число меньше")
        elif guess < secret:
            print("Загаданное число больше")
        else:
            print("Поздравляю! Вы угадали")
            win = True
            break

    if not win:
        print("Вы проиграли. Было загадано: ", secret)

    if not 1 == int(input("Хотите начать сначала? (1 - ДА)\n")):
        break

