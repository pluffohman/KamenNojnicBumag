from random import randint

def gethod(hodpers):
    hodlist = ["Камень", "Ножницы", "Бумага"]
    return hodlist[int(hodpers)-1]

def exit(code):
    print("Выход из программы")
    raise SystemExit(code)

def randhod(hod):
    hodlist = ["Камень", "Ножницы", "Бумага"]
    hodpc = randint(1, 3)
    print(f"Ваш ход: {gethod(hod)}")
    print(f"Ход компьютера: {gethod(hodpc)}")
    hodprogr = gethod(hod)
    win = checkwin(hod, hodpc)
    if win == 0:
        print("Ничья!")
        return hod
    elif win == 1:
        print("Ты победил!")
        return hod
    elif win == 2:
        print("Победила программа!")
        return hod

def checkwin(hodpers, hodpc):
    hodpers1 = gethod(hodpers)
    hodpc1 = gethod(hodpc)
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

def cleverhod(hod):
    vremhod = gethod(hod)
    if vremhod == "Камень":
        hodpc = 3
    elif vremhod == "Бумага":
        hodpc = 2
    elif vremhod == "Ножницы":
        hodpc = 1
    print(f"Ваш ход: {gethod(hod)}")
    print(f"Ход компьютера: {gethod(hodpc)}")
    win = checkwin(hod, hodpc)
    if win == 0:
        print("Ничья!")
        return 0
    elif win == 1:
        print("Ты победил!")
        return 1
    elif win == 2:
        print("Победила программа!")
        return 2

def main():
    hodlist = []
    hodpc = 0
    hodpers = 0
    iter = 0
    print("Программа для игры в камень-ножницы-бумага с компьютером")
    while True:
        iter += 1
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
        hodlist.append(hod)
        print("Выберите стратегию игры программы:")
        print("1) Random")
        print("2) Clever")
        if iter >= 2:
            print("3) Depends on your previous moves")
        cmd = int(input())
        if cmd == 1:
            winreggg = randhod(hod)
        elif cmd == 2:
            winreggg = cleverhod(hod)
        elif cmd == 3:
            winreggg = previoushod(hod)


main()
