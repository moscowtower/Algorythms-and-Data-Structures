from random import randint

def guessGame(correct=None, counter=None):
    if correct == None:
        correct = randint(0, 100)
        print('Я загадал новое число.')
        counter = 0
    if counter == 10:
        q = input(f'К сожалению, попытки кончились. Загаданное число было {correct}. Может сыграем еще разок? д/н:').strip()
        return guessGame() if q == 'д'else 'Хорошо. Приходи, если передумаешь!'
    try:
        ans = int(input('Ваш вариант?: '))
    except ValueError:
        print('Ошибка ввода. Попробуйте еще раз.')
        return guessGame(correct, counter)
    if ans == correct:
        print(f'Поздравляю! Вы отгадали число {correct}')
        return
    elif ans < correct:
        print(f'Неверно. Мое число больше чем {ans}')
    else:
        print(f'Неверно. Мое число меньше чем {ans}')
    counter+=1
    return guessGame(correct, counter)

guessGame()