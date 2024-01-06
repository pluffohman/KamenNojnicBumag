from random import randint

#преобразование номера хода в текст
def gethod(hodpers):
    hodlist = ["Камень", "Ножницы", "Бумага"]
    return hodlist[int(hodpers)-1]

def randhod(hod, hodlist):
    #выбирает рандомный ход из списка
    #hodlist = ["Камень", "Ножницы", "Бумага"]
    hodpc = randint(1, 3)
    #функция вернет ход текстом
    vremhod = gethod(hod)
    #добавляем наш ход в список
    hodlist.append(vremhod)
    print(f"Ваш ход: {gethod(hod)}")
    print(f"Ход компьютера: {gethod(hodpc)}")
    hodprogr = gethod(hod)
    #проверка на победителя
    win = checkwin(hod, hodpc)
    if win == 0:
        print("Ничья!!")
        return 0
    elif win == 1:
        print("Ты победил!")
        return 1
    elif win == 2:
        print("Победила программа!")
        return 2

#проверка на победителя. 0 - ничья, 1 - победа игрока, 2 - победа программы
def checkwin(hodpers, hodpc):
    #получаем наши ходы в текстовом формате
    hodpers1 = gethod(hodpers)
    hodpc1 = gethod(hodpc)
    # 0 - ничья, 1 - победа игрока, 2 - победа программы
    if hodpers1 == hodpc1:
        return 0
    if hodpers1 == "Камень" and hodpc1 == "Ножницы":
        return 1
    if hodpers1 == "Ножницы" and hodpc1 == "Камень":
        return 2
    if hodpers1 == "Бумага" and hodpc1 == "Камень":
        return 1
    if hodpers1 == "Камень" and hodpc1 == "Бумага":
        return 2
    if hodpers1 == "Ножницы" and hodpc1 == "Бумага":
        return 1
    if hodpers1 == "Бумага" and hodpc1 == "Ножницы":
        return 2


#компьютер всегда выигрывает
def cleverhod(hod, hodlist):
    # функция вернет ход текстом
    vremhod = gethod(hod)
    # добавляем наш ход в список
    hodlist.append(vremhod)
    if vremhod == "Камень":
        hodpc = 3
    elif vremhod == "Бумага":
        hodpc = 2
    elif vremhod == "Ножницы":
        hodpc = 1
    #вывод ходов на экран
    print(f"Ваш ход: {gethod(hod)}")
    print(f"Ход компьютера: {gethod(hodpc)}")
    #проверка на победителя
    win = checkwin(hod, hodpc)
    if win == 0:
        print("Ничья!")
        return 0
    elif win == 1:
        print("Ты победил!!")
        return 1
    elif win == 2:
        print("Победила программа!")
        return 2


#смотрим на предыдущие ходы
#Данная функция работает по следующему принципу.
#Если 2 прошлых хода были одинаковыми, то игрок сходит также, что и понимает программа
def previoushod_1(hod, hodlist):
    # функция вернет ход текстом
    vremhod = gethod(hod)
    vr1 = hodlist[-1]
    vr2 = hodlist[-2]
    if vr1 == vr2:
        if vr1 == "Камень":
            hodpc = 3
        elif vr1 == "Бумага":
            hodpc = 2
        elif vr1 == "Ножницы":
            hodpc = 1
    else: #если предыдущие ходы не были одинаковыми, нет смысла искать закономерности
        return randhod(hod,hodlist)
    print(f"Ваш ход: {gethod(hod)}")
    print(f"Ход компьютера: {gethod(hodpc)}")
    # добавляем наш ход в список
    hodlist.append(vremhod)
    # проверка на победителя
    win = checkwin(hod, hodpc)
    if win == 0:
        print("Ничья!!")
        return 0
    elif win == 1:
        print("Ты победил!")
        return 1
    elif win == 2:
        print("Победила программа!")
        return 2

#Данная функция работает по следующему принципу:
#Если 2 раза подряд были одинаковые ходы, то этот, возможно, будет противоположным
def previoushod_2(hod,hodlist):
    # функция вернет ход текстом
    vremhod = gethod(hod)
    vr1 = hodlist[-1]
    vr2 = hodlist[-2]
    if vr1 == vr2:
        if vr1 == "Камень":
            hodpc = 1
        elif vr1 == "Бумага":
            hodpc = 2
        elif vr1 == "Ножницы":
            hodpc = 3
    else: #если предыдущие ходы не были одинаковыми, нет смысла искать закономерности
        return randhod(hod,hodlist)

    print(f"Ваш ход: {gethod(hod)}")
    print(f"Ход компьютера: {gethod(hodpc)}")
    # добавляем наш ход в список
    hodlist.append(vremhod)
    # проверка на победителя
    win = checkwin(hod, hodpc)
    if win == 0:
        print("Ничья!")
        return 0
    elif win == 1:
        print("Ты победил!!")
        return 1
    elif win == 2:
        print("Победила программа!")
        return 2


def main():
    #список ходов
    hodlist = []
    hodpc = 0
    hodpers = 0
    iter = 0
    print("Программа для игры в камень-ножницы-бумага с компьютером")
    while True:
        print("Выберите ход: ")
        print("1) Камень")
        print("2) Ножницы")
        print("3) Бумага")
        print("4) Показать счет")
        print("0) Выход")
        hod = int(input())
        if hod == 0:
            exit(0)
        elif hod == 4:
            print("Пк : игрок")
            print(f"{hodpc} : {hodpers}")
            continue
        print("Выберите стратегию игры программы:")
        print("1) Random")
        print("2) Clever")
        #данные режимы доступны только после двух уже сделанных ходов
        if iter >= 2:
            print("3) Depends on your previous moves 1")
            print("4) Depends on your previous moves 2")
        cmd = int(input())
        if cmd == 1:
            winreggg = randhod(hod, hodlist)
        elif cmd == 2:
            winreggg = cleverhod(hod, hodlist)
        elif cmd == 3:
            winreggg = previoushod_1(hod, hodlist)
        elif cmd == 4:
            winreggg = previoushod_2(hod, hodlist)


        #добавление очков победителю
        if winreggg == 1:
            hodpers += 1
        elif winreggg == 2:
            hodpc += 1


        iter += 1

#запуск программы
if __name__ == "__main__":
    main()
