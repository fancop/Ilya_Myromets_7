import os
import random

name = input("как зовут персонажа? ")
if not name: name = "Илья Муромец"

way_1 = True
way_2 = True
way_3 = True
game = True
key = ""
user_health = 100
outlaw_health = 100
user_money = 10
casino_money = 10

while game:

    #камень
    if (way_1 or way_2 or way_3) and key == "":
        key = ""
        os.system("cls")
        print(f"{name} у камня")
        if way_1:
            print("1 вариант")
        if way_2:
            print("2 вариант")
        if way_3:
            print("3 вариант")
        user_choice = input("какой вариант? ")

        if user_choice == "1" or user_choice == "2" or user_choice == "3":
            key += user_choice

    # 1 дорога
    if key == "1" and way_1:
        os.system("cls")
        while user_health > 0 and outlaw_health > 0:
            os.system("cls")

            user_damage = random.randint(1, 10)
            outlaw_health -= user_damage
            print("Игрок нанёс разбойнику", user_damage, "ХП")
            print("У разбойника осталось", outlaw_health, "ХП")

            outlaw_damage = random.randint(1, 10)
            user_health -= outlaw_damage
            print("Разбойник нанёс игроку", outlaw_damage, "ХП")
            print("У игрока осталось", user_health, "ХП")

            input("Нажмите ENTER, что-бы продолжить")

            if user_health > 0:
                print("игрок победил")

                way_1 = False
                key = ""
            else:
                print("разбойник победил")
                game = False

    # 2 дорога
    if key == "2" and way_2:
        os.system("cls")
        import random
        secret = random.randint(1, 100)

        print("Княжна загадала число от 1 до 100. Угадай его.")

        attempts = 7
        while attempts:
            print(f"у тебя {attempts} попыток")
            user_choice = int(input("введите число: "))
            if user_choice == secret:
                print("угадал")
                input("нажмите ENTER что-бы подолжить")
                key = "" # выигрыш
                way_2 = False
                break
            elif user_choice > secret:
                print("многовато")
                attempts -= 1
            else:
                print("маловато")
                attempts -= 1
        else:
            print("проиграл попытки кончились")
            game = False # проигрыш



    # 3 дорога
    if key == "3" and way_3:
        os.system("cls")
        while user_money and casino_money:

            #сколько у кого денег
            print("у игрока", user_money, "монет")

            input("нажмите ENTER что-бы делать ход")
            #делаем ходы
            user_turn = random.randint(1, 6)
            casino_turn = random.randint(1, 6)
            print("игрок выбросил", user_turn)
            print("казино выбросило", casino_turn)


            #считаем, кто выйграл
            if user_turn > casino_turn:
                print("игрок победил")
                user_money+=1
                casino_money-=1
            elif casino_turn > user_turn:
                print("казино победило")
                casino_money+=1
                user_money-=1
            else:
                print("ничья")

            if casino_money == 0:
                print("игрок забрал все деньги")
            else:
                game = False

            if way_1 == way_2 == way_3 == False:
                print("ура мы победили")
                game = False

print("Ура я победил")