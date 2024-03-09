from random import randint, choice
from time import sleep


def get_result(deal_score: int, player_score: int) -> None:
    """Print game result
    :params: deal_score: int, player_score: int
    :return: None"""
    print(f"{'-' * 20}")
    print(f"Результат раунда:\nИгрок: {player_score}\nДиллер: {deal_score}")
    print(f"{'-' * 20}")


def throw_dice() -> int:
    """Return result of throwing a dice
    :return: int - throwing result(1 - 11)"""
    return randint(1, 11)


def dealer_act() -> str:
    """Return dealer act(hit, hold or end)
    :return: str"""
    acts = ("hit", "hold", "end", "hit", "hit", "hold")
    return choice(acts)


def player_act(score: int) -> str:
    """Return player act(hit, hold or end)
    :params: score: int player score for input showing
    :return: str"""
    while (act := input(f"hit, hold or end\n{score} > ")) not in ("hit", "hold", "end"):
        print("Неправильный/неизвестный ввод")
    return act
    

def play():
    """Main fuction, here will be a game"""
    print(f"""{'-' * 20}
    начало игры\n{'-' * 20}""")
    dealer = player = 0
    player_can, dealer_can = True, True
    while True:
        if player_can:
            act = player_act(player)
            print(f"{'-' * 20}")
            if act == "hit":
                throw = throw_dice()
                player += throw
                print(f"Результат броска Игрока: {throw}")
                if player > 21:
                    print(f"Дилер победил. Счёт игры:\nИгрок: {player}\nДиллер: {dealer}")
                    return
                
            elif act == "end":
                player_can = False
            else:
                pass
            sleep(1)
        if dealer_can:
            deal_act = dealer_act()
            print(f"Выбор Диллера: {deal_act}")
            if deal_act == "hit":
                throw = throw_dice()
                dealer += throw
                print(f"Результат броска Диллера: {throw}")
                if dealer > 21:
                    print(f"Игрок победил. Счёт игры:\nИгрок: {player}\nДиллер: {dealer}")
                    return
            elif deal_act == "end":
                dealer_can = False
            elif deal_act == "hold":
                get_result(dealer, player)
                continue
            sleep(1)
        elif not dealer_can and not player_can:
            print(f"Оба выбрали закончить\nПросматриваем результат...\nИгрок: {player}\nДиллер: {dealer}")
            if dealer < player:
                print("Игрок победил")
            elif dealer > player:
                print("Диллер победил")
            else:
                print("Ничья")
            return
        sleep(1)
        get_result(dealer, player)

    


while True:
    play()
    input("Press enter to continue\n> ")