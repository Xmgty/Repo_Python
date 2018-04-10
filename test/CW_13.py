from random import shuffle
deck = [6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']*4
print("Игра Очко. Выберите режим: ")
choice = int(input("1. Одиночная игра"))
player = {}
shuler = {}
def shulers(deck):
    card = deck.pop()
    shuler[1] = card
    card2 = deck.pop()
    shuler[2] = card2
    return shuler

def addshulers(deck):
    cardadd = deck.pop()
    shuler[3] = cardadd
    return shuler

def addshulers2(deck):
    cardadd = deck.pop()
    shuler[4] = cardadd
    return shuler

def addshulers3(deck):
    cardadd = deck.pop()
    shuler[5] = cardadd
    return shuler

def countsh(shuler):
    count1 = 0
    tuzcount = 0
    for q in shuler:
        if type(shuler[q]) == int:
            count1 += shuler[q]
        else:
            if shuler[q] == 'J':
                count1 += 2
            if shuler[q] == 'Q':
                count1 += 3
            if shuler[q] == 'K':
                count1 += 4
            if shuler[q] == 'A':
                count1 += 11
                tuzcount += 1
    if count1 > 21 and tuzcount == 1:
        count1 -= 10
        tuzcount -= 0
    return count1


def setcard(deck):
    card = deck.pop()
    player[1]= card
    card2 = deck.pop()
    player[2]= card2
    print(deck)
    return player
def addcard(deck):
    cardadd = deck.pop()
    player[3]=cardadd
    print(deck)
    return player
def addcard2(deck):
    cardadd = deck.pop()
    player[4]=cardadd
    print(deck)
    return player
def addcard3(deck):
    cardadd = deck.pop()
    player[5]=cardadd
    print(deck)
    return player
def addcard4(deck):
    cardadd = deck.pop()
    player[6]=cardadd
    print(deck)
    return player
def count(player):
    count1 = 0
    tuzcount = 0
    for q in player:
        if type(player[q]) == int:
            count1 += player[q]
        else:
            if player[q] == 'J':
                count1 += 2
            if player[q] == 'Q':
                count1 += 3
            if player[q] == 'K':
                count1 += 4
            if player[q] == 'A':
                count1 += 11
                tuzcount += 1
    if count1 > 21 and tuzcount == 1:
        count1 -= 10
        tuzcount -= 0
    return count1

if choice == 1:
    print("Выбран режим одииночной игры")
    print("Тасуем карты...")
    shuffle(deck)
    print(deck)
    print(shulers(deck))
    print(countsh(shuler))
    if countsh(shuler) < 17:
        print(addshulers(deck))
        print(countsh(shuler))
        if countsh(shuler) < 17:
            print(addshulers2(deck))
            print(countsh(shuler))
            if countsh(shuler) < 17:
                print(addshulers3(deck))
                print(countsh(shuler))
    print(setcard(deck))
    print(count(player))
    choicecon = input("Желаете ещё карту? Y/N")
    if choicecon == 'Y' or choicecon == 'y':
        print(addcard(deck))
        print(count(player))
        if count(player) == 21:
            print("Очко! Вы победили!")
        elif count(player) > 21:
            print("Перебор! Вы проиграли!")
        else:
            choicecon = input("Желаете ещё карту? Y/N")
            if choicecon == 'Y' or choicecon == 'y':
                print(addcard3(deck))
                print(count(player))
                if count(player) == 21:
                    print("Очко! Вы победили!")
                elif count(player) > 21:
                    print("Перебор! Вы проиграли!")
                else:
                    choicecon = input("Желаете ещё карту? Y/N")
                    if choicecon == 'Y' or choicecon == 'y':
                        print(addcard4(deck))
                        print(count(player))
                        if count(player) == 21:
                            print("Очко! Вы победили!")
                        elif count(player) > 21:
                            print("Перебор! Вы проиграли!")
    else:
        print("Ход окончен. Ваш счет -")
        print(count(player))
