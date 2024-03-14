import random
from decouple import config
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def game():
    my_money = config('MY_MONEY', cast=int)
    while True:
        input_number = int(input('Введите номер слота(1-10): '))
        print(f"Ваш текущий капитал: {my_money}$")
        bet = int(input("Введите сумму ставки (0 для выхода): "))
        if bet == 0:
            break
        if bet > my_money:
            print("Сумма ставки превышает ваш текущий капитал!")
            continue
        slot = random.choice(list1)
        print(f"Вы выбрали слоту: {input_number}")
        if slot == input_number:
            bet += bet * 2
            print("Вы выиграли! Ваш капитал удвоен.")
        else:
            my_money -= bet
            print("Вы проиграли. Ваш капитал уменьшен.")
            print(f"Итог игры: {my_money} 💵")





