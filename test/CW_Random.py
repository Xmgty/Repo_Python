import random
from os import system


mode = 1
a = 1
end = 1
help = 0
nova = 0

while mode != 0:
    print("Игра Кубики. Выберите режим игры.")
    print("1. Одиночная игра")
    print("2. Два игрока")
    print("0. Выход из игры")
    mode = int(input("Вводите тут >>> "))
    if mode == 1:
        while end != 'stop':
            print("Игра Кубики. Режим одиночной игры.")
            print("Ход -", a)
            print("Угадай число (1-12). Или набери stop для выхода в главное меню")
            end = input("Ну давай вводи: ")
            if end == 'Stop' or end == 'stop':
                break
            bone1 = random.randint(1, 6)
            bone2 = random.randint(1, 6)
            sum = bone1 + bone2
            print(bone1 + bone2)
            if bone1 == 1 and bone2 == 1:
                print("* * * * *     * * * * *")
                print("*       *     *       *")
                print("*   @   *     *   @   *")
                print("*       *     *       *")
                print("* * * * *     * * * * *")
            if bone1 == 1 and bone2 == 2:
                print("* * * * *     * * * * *")
                print("*       *     *     @ *")
                print("*   @   *     *       *")
                print("*       *     * @     *")
                print("* * * * *     * * * * *")
            if bone1 == 1 and bone2 == 3:
                print("* * * * *     * * * * *")
                print("*       *     *     @ *")
                print("*   @   *     *   @   *")
                print("*       *     * @     *")
                print("* * * * *     * * * * *")
            if bone1 == 1 and bone2 == 4:
                print("* * * * *     * * * * *")
                print("*       *     * @   @ *")
                print("*   @   *     *       *")
                print("*       *     * @   @ *")
                print("* * * * *     * * * * *")
            if bone1 == 1 and bone2 == 5:
                print("* * * * *     * * * * *")
                print("*       *     * @   @ *")
                print("*   @   *     *   @   *")
                print("*       *     * @   @ *")
                print("* * * * *     * * * * *")
            if bone1 == 1 and bone2 == 6:
                print("* * * * *     * * * * *")
                print("*       *     * @   @ *")
                print("*   @   *     * @   @ *")
                print("*       *     * @   @ *")
                print("* * * * *     * * * * *")
            if bone1 == 2 and bone2 == 1:
                print("* * * * *     * * * * *")
                print("*    @  *     *       *")
                print("*       *     *   @   *")
                print("* @     *     *       *")
                print("* * * * *     * * * * *")
            if bone1 == 2 and bone2 == 2:
                print("* * * * *     * * * * *")
                print("*     @ *     *     @ *")
                print("*       *     *       *")
                print("* @     *     * @     *")
                print("* * * * *     * * * * *")
            if bone1 == 2 and bone2 == 3:
                print("* * * * *     * * * * *")
                print("*     @ *     *     @ *")
                print("*       *     *   @   *")
                print("* @     *     * @     *")
                print("* * * * *     * * * * *")
            if bone1 == 2 and bone2 == 4:
                print("* * * * *     * * * * *")
                print("*     @ *     * @   @ *")
                print("*       *     *       *")
                print("* @     *     * @   @ *")
                print("* * * * *     * * * * *")
            if bone1 == 2 and bone2 == 5:
                print("* * * * *     * * * * *")
                print("*     @ *     * @   @ *")
                print("*       *     *   @   *")
                print("* @     *     * @   @ *")
                print("* * * * *     * * * * *")
            if bone1 == 2 and bone2 == 6:
                print("* * * * *     * * * * *")
                print("*     @ *     * @   @ *")
                print("*       *     * @   @ *")
                print("* @     *     * @   @ *")
                print("* * * * *     * * * * *")
            if bone1 == 3 and bone2 == 1:
                print("* * * * *     * * * * *")
                print("*     @ *     *       *")
                print("*   @   *     *   @   *")
                print("* @     *     *       *")
                print("* * * * *     * * * * *")
            if bone1 == 3 and bone2 == 2:
                print("* * * * *     * * * * *")
                print("*     @ *     *     @ *")
                print("*   @   *     *       *")
                print("* @     *     * @     *")
                print("* * * * *     * * * * *")
            if bone1 == 3 and bone2 == 3:
                print("* * * * *     * * * * *")
                print("*     @ *     *     @ *")
                print("*   @   *     *   @   *")
                print("* @     *     * @     *")
                print("* * * * *     * * * * *")
            if bone1 == 3 and bone2 == 4:
                print("* * * * *     * * * * *")
                print("*     @ *     * @   @ *")
                print("*   @   *     *       *")
                print("* @     *     * @   @ *")
                print("* * * * *     * * * * *")
            if bone1 == 3 and bone2 == 5:
                print("* * * * *     * * * * *")
                print("*     @ *     * @   @ *")
                print("*   @   *     *   @   *")
                print("* @     *     * @   @ *")
                print("* * * * *     * * * * *")
            if bone1 == 3 and bone2 == 6:
                print("* * * * *     * * * * *")
                print("*     @ *     * @   @ *")
                print("*   @   *     * @   @ *")
                print("* @     *     * @   @ *")
                print("* * * * *     * * * * *")
            if bone1 == 4 and bone2 == 1:
                print("* * * * *     * * * * *")
                print("* @   @ *     *       *")
                print("*       *     *   @   *")
                print("* @   @ *     *       *")
                print("* * * * *     * * * * *")
            if bone1 == 4 and bone2 == 2:
                print("* * * * *     * * * * *")
                print("* @   @ *     *     @ *")
                print("*       *     *       *")
                print("* @   @ *     * @     *")
                print("* * * * *     * * * * *")
            if bone1 == 4 and bone2 == 3:
                print("* * * * *     * * * * *")
                print("* @   @ *     *     @ *")
                print("*       *     *   @   *")
                print("* @   @ *     * @     *")
                print("* * * * *     * * * * *")
            if bone1 == 4 and bone2 == 4:
                print("* * * * *     * * * * *")
                print("* @   @ *     * @   @ *")
                print("*       *     *       *")
                print("* @   @ *     * @   @ *")
                print("* * * * *     * * * * *")
            if bone1 == 4 and bone2 == 5:
                print("* * * * *     * * * * *")
                print("* @   @ *     * @   @ *")
                print("*       *     *   @   *")
                print("* @   @ *     * @   @ *")
                print("* * * * *     * * * * *")
            if bone1 == 4 and bone2 == 6:
                print("* * * * *     * * * * *")
                print("* @   @ *     * @   @ *")
                print("*       *     * @   @ *")
                print("* @   @ *     * @   @ *")
                print("* * * * *     * * * * *")
            if bone1 == 5 and bone2 == 1:
                print("* * * * *     * * * * *")
                print("* @   @ *     *       *")
                print("*   @   *     *   @   *")
                print("* @   @ *     *       *")
                print("* * * * *     * * * * *")
            if bone1 == 5 and bone2 == 2:
                print("* * * * *     * * * * *")
                print("* @   @ *     *     @ *")
                print("*   @   *     *       *")
                print("* @   @ *     * @     *")
                print("* * * * *     * * * * *")
            if bone1 == 5 and bone2 == 3:
                print("* * * * *     * * * * *")
                print("* @   @ *     *     @ *")
                print("*   @   *     *   @   *")
                print("* @   @ *     * @     *")
                print("* * * * *     * * * * *")
            if bone1 == 5 and bone2 == 4:
                print("* * * * *     * * * * *")
                print("* @   @ *     * @   @ *")
                print("*   @   *     *       *")
                print("* @   @ *     * @   @ *")
                print("* * * * *     * * * * *")
            if bone1 == 5 and bone2 == 5:
                print("* * * * *     * * * * *")
                print("* @   @ *     * @   @ *")
                print("*   @   *     *   @   *")
                print("* @   @ *     * @   @ *")
                print("* * * * *     * * * * *")
            if bone1 == 5 and bone2 == 6:
                print("* * * * *     * * * * *")
                print("* @   @ *     * @   @ *")
                print("*   @   *     * @   @ *")
                print("* @   @ *     * @   @ *")
                print("* * * * *     * * * * *")
            if bone1 == 6 and bone2 == 1:
                print("* * * * *     * * * * *")
                print("* @   @ *     *       *")
                print("* @   @ *     *   @   *")
                print("* @   @ *     *       *")
                print("* * * * *     * * * * *")
            if bone1 == 6 and bone2 == 2:
                print("* * * * *     * * * * *")
                print("* @   @ *     *     @ *")
                print("* @   @ *     *       *")
                print("* @   @ *     * @     *")
                print("* * * * *     * * * * *")
            if bone1 == 6 and bone2 == 3:
                print("* * * * *     * * * * *")
                print("* @   @ *     *     @ *")
                print("* @   @ *     *   @   *")
                print("* @   @ *     * @     *")
                print("* * * * *     * * * * *")
            if bone1 == 6 and bone2 == 4:
                print("* * * * *     * * * * *")
                print("* @   @ *     * @   @ *")
                print("* @   @ *     *       *")
                print("* @   @ *     * @   @ *")
                print("* * * * *     * * * * *")
            if bone1 == 6 and bone2 == 5:
                print("* * * * *     * * * * *")
                print("* @   @ *     * @   @ *")
                print("* @   @ *     *   @   *")
                print("* @   @ *     * @   @ *")
                print("* * * * *     * * * * *")
            if bone1 == 6 and bone2 == 6:
                print("* * * * *     * * * * *")
                print("* @   @ *     * @   @ *")
                print("* @   @ *     * @   @ *")
                print("* @   @ *     * @   @ *")
                print("* * * * *     * * * * *")

            if sum == end:
                print("Что ты тут забыл? Иди в казино, ты везунчик!")
                a = a + 1
            else:
                print("Ха, не в этот раз, ты лузер")
                a = a + 1

    if mode == 2:
        round1 = 0
        round2 = 0
        eeend1 = 0
        eeend2 = 0
        score1 = 500
        score2 = 500
        bet1 = 0
        bet2 = 0
        chance1 = 0
        chance2 = 0
        woop = 0
        print("Игра Кубики. Режим два игрока. Старт с 500 очков, каждый игрок может делать ставку. Игра закончится когда один из игроков наберет 1000 очков или обанкротится")
        print("Игроки могут указывать за сколько раундов они отгадают(от 1 до 5) от этого зависит размер выйгрыша. 1 ход x2, 2 x 1.9, 3 x 1.8 и т.д.")
        while score1 > 0 or score2 > 0 or score1 < 1000 or score2 > 1000 or eeend1 != 'stop':
             eeend1 = input("Нажмите что-нибудь, чтобы продолжить (any key for yes or 'stop' to exit)")
             print("Определяем очерёдность ходов...")
             turn = 1
             round1 = 0
             round2 = 0
             chance1 = 0
             chance2 = 0
             if turn == 1:
                 nova = 0
                 print("Начинает первый игрок")
                 bet1 = input("Назовите вашу ставку >>")
                 chance1 = int(input("Количество раундов для угадывания?"))
                 for nova in range(1):
                     while round1 != chance1:
                         print("Раунд -", round1+1)
                         eeend1 = input("Ну давай вводи Игрок1: ")
                         if eeend1 == 'stop' or bet1 == 'stop' or chance1 == 'stop' or bet2 == 'stop':
                            break
                         else:
                            bone1 = random.randint(1, 6)
                            bone2 = random.randint(1, 6)
                            sum = bone1 + bone2
                            print(bone1 + bone2)
                            if bone1 == 1 and bone2 == 1:
                                print("* * * * *     * * * * *")
                                print("*       *     *       *")
                                print("*   @   *     *   @   *")
                                print("*       *     *       *")
                                print("* * * * *     * * * * *")
                            if bone1 == 1 and bone2 == 2:
                                print("* * * * *     * * * * *")
                                print("*       *     *     @ *")
                                print("*   @   *     *       *")
                                print("*       *     * @     *")
                                print("* * * * *     * * * * *")
                            if bone1 == 1 and bone2 == 3:
                                print("* * * * *     * * * * *")
                                print("*       *     *     @ *")
                                print("*   @   *     *   @   *")
                                print("*       *     * @     *")
                                print("* * * * *     * * * * *")
                            if bone1 == 1 and bone2 == 4:
                                print("* * * * *     * * * * *")
                                print("*       *     * @   @ *")
                                print("*   @   *     *       *")
                                print("*       *     * @   @ *")
                                print("* * * * *     * * * * *")
                            if bone1 == 1 and bone2 == 5:
                                print("* * * * *     * * * * *")
                                print("*       *     * @   @ *")
                                print("*   @   *     *   @   *")
                                print("*       *     * @   @ *")
                                print("* * * * *     * * * * *")
                            if bone1 == 1 and bone2 == 6:
                                print("* * * * *     * * * * *")
                                print("*       *     * @   @ *")
                                print("*   @   *     * @   @ *")
                                print("*       *     * @   @ *")
                                print("* * * * *     * * * * *")
                            if bone1 == 2 and bone2 == 1:
                                print("* * * * *     * * * * *")
                                print("*    @  *     *       *")
                                print("*       *     *   @   *")
                                print("* @     *     *       *")
                                print("* * * * *     * * * * *")
                            if bone1 == 2 and bone2 == 2:
                                print("* * * * *     * * * * *")
                                print("*     @ *     *     @ *")
                                print("*       *     *       *")
                                print("* @     *     * @     *")
                                print("* * * * *     * * * * *")
                            if bone1 == 2 and bone2 == 3:
                                print("* * * * *     * * * * *")
                                print("*     @ *     *     @ *")
                                print("*       *     *   @   *")
                                print("* @     *     * @     *")
                                print("* * * * *     * * * * *")
                            if bone1 == 2 and bone2 == 4:
                                print("* * * * *     * * * * *")
                                print("*     @ *     * @   @ *")
                                print("*       *     *       *")
                                print("* @     *     * @   @ *")
                                print("* * * * *     * * * * *")
                            if bone1 == 2 and bone2 == 5:
                                print("* * * * *     * * * * *")
                                print("*     @ *     * @   @ *")
                                print("*       *     *   @   *")
                                print("* @     *     * @   @ *")
                                print("* * * * *     * * * * *")
                            if bone1 == 2 and bone2 == 6:
                                print("* * * * *     * * * * *")
                                print("*     @ *     * @   @ *")
                                print("*       *     * @   @ *")
                                print("* @     *     * @   @ *")
                                print("* * * * *     * * * * *")
                            if bone1 == 3 and bone2 == 1:
                                print("* * * * *     * * * * *")
                                print("*     @ *     *       *")
                                print("*   @   *     *   @   *")
                                print("* @     *     *       *")
                                print("* * * * *     * * * * *")
                            if bone1 == 3 and bone2 == 2:
                                print("* * * * *     * * * * *")
                                print("*     @ *     *     @ *")
                                print("*   @   *     *       *")
                                print("* @     *     * @     *")
                                print("* * * * *     * * * * *")
                            if bone1 == 3 and bone2 == 3:
                                print("* * * * *     * * * * *")
                                print("*     @ *     *     @ *")
                                print("*   @   *     *   @   *")
                                print("* @     *     * @     *")
                                print("* * * * *     * * * * *")
                            if bone1 == 3 and bone2 == 4:
                                print("* * * * *     * * * * *")
                                print("*     @ *     * @   @ *")
                                print("*   @   *     *       *")
                                print("* @     *     * @   @ *")
                                print("* * * * *     * * * * *")
                            if bone1 == 3 and bone2 == 5:
                                print("* * * * *     * * * * *")
                                print("*     @ *     * @   @ *")
                                print("*   @   *     *   @   *")
                                print("* @     *     * @   @ *")
                                print("* * * * *     * * * * *")
                            if bone1 == 3 and bone2 == 6:
                                print("* * * * *     * * * * *")
                                print("*     @ *     * @   @ *")
                                print("*   @   *     * @   @ *")
                                print("* @     *     * @   @ *")
                                print("* * * * *     * * * * *")
                            if bone1 == 4 and bone2 == 1:
                                print("* * * * *     * * * * *")
                                print("* @   @ *     *       *")
                                print("*       *     *   @   *")
                                print("* @   @ *     *       *")
                                print("* * * * *     * * * * *")
                            if bone1 == 4 and bone2 == 2:
                                print("* * * * *     * * * * *")
                                print("* @   @ *     *     @ *")
                                print("*       *     *       *")
                                print("* @   @ *     * @     *")
                                print("* * * * *     * * * * *")
                            if bone1 == 4 and bone2 == 3:
                                print("* * * * *     * * * * *")
                                print("* @   @ *     *     @ *")
                                print("*       *     *   @   *")
                                print("* @   @ *     * @     *")
                                print("* * * * *     * * * * *")
                            if bone1 == 4 and bone2 == 4:
                                print("* * * * *     * * * * *")
                                print("* @   @ *     * @   @ *")
                                print("*       *     *       *")
                                print("* @   @ *     * @   @ *")
                                print("* * * * *     * * * * *")
                            if bone1 == 4 and bone2 == 5:
                                print("* * * * *     * * * * *")
                                print("* @   @ *     * @   @ *")
                                print("*       *     *   @   *")
                                print("* @   @ *     * @   @ *")
                                print("* * * * *     * * * * *")
                            if bone1 == 4 and bone2 == 6:
                                print("* * * * *     * * * * *")
                                print("* @   @ *     * @   @ *")
                                print("*       *     * @   @ *")
                                print("* @   @ *     * @   @ *")
                                print("* * * * *     * * * * *")
                            if bone1 == 5 and bone2 == 1:
                                print("* * * * *     * * * * *")
                                print("* @   @ *     *       *")
                                print("*   @   *     *   @   *")
                                print("* @   @ *     *       *")
                                print("* * * * *     * * * * *")
                            if bone1 == 5 and bone2 == 2:
                                print("* * * * *     * * * * *")
                                print("* @   @ *     *     @ *")
                                print("*   @   *     *       *")
                                print("* @   @ *     * @     *")
                                print("* * * * *     * * * * *")
                            if bone1 == 5 and bone2 == 3:
                                print("* * * * *     * * * * *")
                                print("* @   @ *     *     @ *")
                                print("*   @   *     *   @   *")
                                print("* @   @ *     * @     *")
                                print("* * * * *     * * * * *")
                            if bone1 == 5 and bone2 == 4:
                                print("* * * * *     * * * * *")
                                print("* @   @ *     * @   @ *")
                                print("*   @   *     *       *")
                                print("* @   @ *     * @   @ *")
                                print("* * * * *     * * * * *")
                            if bone1 == 5 and bone2 == 5:
                                print("* * * * *     * * * * *")
                                print("* @   @ *     * @   @ *")
                                print("*   @   *     *   @   *")
                                print("* @   @ *     * @   @ *")
                                print("* * * * *     * * * * *")
                            if bone1 == 5 and bone2 == 6:
                                print("* * * * *     * * * * *")
                                print("* @   @ *     * @   @ *")
                                print("*   @   *     * @   @ *")
                                print("* @   @ *     * @   @ *")
                                print("* * * * *     * * * * *")
                            if bone1 == 6 and bone2 == 1:
                                print("* * * * *     * * * * *")
                                print("* @   @ *     *       *")
                                print("* @   @ *     *   @   *")
                                print("* @   @ *     *       *")
                                print("* * * * *     * * * * *")
                            if bone1 == 6 and bone2 == 2:
                                print("* * * * *     * * * * *")
                                print("* @   @ *     *     @ *")
                                print("* @   @ *     *       *")
                                print("* @   @ *     * @     *")
                                print("* * * * *     * * * * *")
                            if bone1 == 6 and bone2 == 3:
                                print("* * * * *     * * * * *")
                                print("* @   @ *     *     @ *")
                                print("* @   @ *     *   @   *")
                                print("* @   @ *     * @     *")
                                print("* * * * *     * * * * *")
                            if bone1 == 6 and bone2 == 4:
                                print("* * * * *     * * * * *")
                                print("* @   @ *     * @   @ *")
                                print("* @   @ *     *       *")
                                print("* @   @ *     * @   @ *")
                                print("* * * * *     * * * * *")
                            if bone1 == 6 and bone2 == 5:
                                print("* * * * *     * * * * *")
                                print("* @   @ *     * @   @ *")
                                print("* @   @ *     *   @   *")
                                print("* @   @ *     * @   @ *")
                                print("* * * * *     * * * * *")
                            if bone1 == 6 and bone2 == 6:
                                print("* * * * *     * * * * *")
                                print("* @   @ *     * @   @ *")
                                print("* @   @ *     * @   @ *")
                                print("* @   @ *     * @   @ *")
                                print("* * * * *     * * * * *")
                            if sum == int(eeend1):
                                print("Молодец! Угадал")
                                if chance1 == 1:
                                    print("Нифига ты монстр!")
                                    score1 = score1 + (int(bet1)*2)
                                    print("Твой счет -", score1)
                                    print("Счет игрока №2 -", score2)
                                    break
                                if chance1 == 2:
                                    score1 = score1 + (int(bet1) * 1.9)
                                    print("Твой счет -", score1)
                                    print("Счет игрока №2 -", score2)
                                    break
                                if chance1 == 3:
                                    score1 = score1 + (int(bet1) * 1.8)
                                    print("Твой счет -", score1)
                                    print("Счет игрока №2 -", score2)
                                    break
                                if chance1 == 4:
                                    score1 = score1 + (int(bet1) * 1.7)
                                    print("Твой счет -", score1)
                                    print("Счет игрока №2 -", score2)
                                    break
                                if chance1 == 5:
                                    score1 = score1 + (int(bet1) * 1.6)
                                    print("Твой счет -", score1)
                                    print("Счет игрока №2 -", score2)
                                    break
                            else:
                                print("Не угадал!")
                                round1 = round1 + 1
                                if chance1 == (round1):
                                   print("Твои попытки закончились")
                                   score1 = score1 - int(bet1)
                                   print("Твой счет -", score1)
                                   print("Счет игрока №2 -", score2)

                     print("Ход игрока №2")
                     bet2 = input("Назовите вашу ставку >>")
                     chance2 = int(input("Количество раундов для угадывания?"))

                     while chance2 != round2:
                         print("Раунд -", round2 + 1)
                         eeend2 = input("Ну давай вводи Игрок2: ")
                         if eeend2 == 'stop' or bet2 == 'stop' or chance2 == 'stop' or bet2 == 'stop':
                             break

                         else:
                             bone1 = random.randint(1, 6)
                             bone2 = random.randint(1, 6)
                             sum = bone1 + bone2
                             print(bone1 + bone2)
                             if bone1 == 1 and bone2 == 1:
                                 print("* * * * *     * * * * *")
                                 print("*       *     *       *")
                                 print("*   @   *     *   @   *")
                                 print("*       *     *       *")
                                 print("* * * * *     * * * * *")
                             if bone1 == 1 and bone2 == 2:
                                 print("* * * * *     * * * * *")
                                 print("*       *     *     @ *")
                                 print("*   @   *     *       *")
                                 print("*       *     * @     *")
                                 print("* * * * *     * * * * *")
                             if bone1 == 1 and bone2 == 3:
                                 print("* * * * *     * * * * *")
                                 print("*       *     *     @ *")
                                 print("*   @   *     *   @   *")
                                 print("*       *     * @     *")
                                 print("* * * * *     * * * * *")
                             if bone1 == 1 and bone2 == 4:
                                 print("* * * * *     * * * * *")
                                 print("*       *     * @   @ *")
                                 print("*   @   *     *       *")
                                 print("*       *     * @   @ *")
                                 print("* * * * *     * * * * *")
                             if bone1 == 1 and bone2 == 5:
                                 print("* * * * *     * * * * *")
                                 print("*       *     * @   @ *")
                                 print("*   @   *     *   @   *")
                                 print("*       *     * @   @ *")
                                 print("* * * * *     * * * * *")
                             if bone1 == 1 and bone2 == 6:
                                 print("* * * * *     * * * * *")
                                 print("*       *     * @   @ *")
                                 print("*   @   *     * @   @ *")
                                 print("*       *     * @   @ *")
                                 print("* * * * *     * * * * *")
                             if bone1 == 2 and bone2 == 1:
                                 print("* * * * *     * * * * *")
                                 print("*    @  *     *       *")
                                 print("*       *     *   @   *")
                                 print("* @     *     *       *")
                                 print("* * * * *     * * * * *")
                             if bone1 == 2 and bone2 == 2:
                                 print("* * * * *     * * * * *")
                                 print("*     @ *     *     @ *")
                                 print("*       *     *       *")
                                 print("* @     *     * @     *")
                                 print("* * * * *     * * * * *")
                             if bone1 == 2 and bone2 == 3:
                                 print("* * * * *     * * * * *")
                                 print("*     @ *     *     @ *")
                                 print("*       *     *   @   *")
                                 print("* @     *     * @     *")
                                 print("* * * * *     * * * * *")
                             if bone1 == 2 and bone2 == 4:
                                 print("* * * * *     * * * * *")
                                 print("*     @ *     * @   @ *")
                                 print("*       *     *       *")
                                 print("* @     *     * @   @ *")
                                 print("* * * * *     * * * * *")
                             if bone1 == 2 and bone2 == 5:
                                 print("* * * * *     * * * * *")
                                 print("*     @ *     * @   @ *")
                                 print("*       *     *   @   *")
                                 print("* @     *     * @   @ *")
                                 print("* * * * *     * * * * *")
                             if bone1 == 2 and bone2 == 6:
                                 print("* * * * *     * * * * *")
                                 print("*     @ *     * @   @ *")
                                 print("*       *     * @   @ *")
                                 print("* @     *     * @   @ *")
                                 print("* * * * *     * * * * *")
                             if bone1 == 3 and bone2 == 1:
                                 print("* * * * *     * * * * *")
                                 print("*     @ *     *       *")
                                 print("*   @   *     *   @   *")
                                 print("* @     *     *       *")
                                 print("* * * * *     * * * * *")
                             if bone1 == 3 and bone2 == 2:
                                 print("* * * * *     * * * * *")
                                 print("*     @ *     *     @ *")
                                 print("*   @   *     *       *")
                                 print("* @     *     * @     *")
                                 print("* * * * *     * * * * *")
                             if bone1 == 3 and bone2 == 3:
                                 print("* * * * *     * * * * *")
                                 print("*     @ *     *     @ *")
                                 print("*   @   *     *   @   *")
                                 print("* @     *     * @     *")
                                 print("* * * * *     * * * * *")
                             if bone1 == 3 and bone2 == 4:
                                 print("* * * * *     * * * * *")
                                 print("*     @ *     * @   @ *")
                                 print("*   @   *     *       *")
                                 print("* @     *     * @   @ *")
                                 print("* * * * *     * * * * *")
                             if bone1 == 3 and bone2 == 5:
                                 print("* * * * *     * * * * *")
                                 print("*     @ *     * @   @ *")
                                 print("*   @   *     *   @   *")
                                 print("* @     *     * @   @ *")
                                 print("* * * * *     * * * * *")
                             if bone1 == 3 and bone2 == 6:
                                 print("* * * * *     * * * * *")
                                 print("*     @ *     * @   @ *")
                                 print("*   @   *     * @   @ *")
                                 print("* @     *     * @   @ *")
                                 print("* * * * *     * * * * *")
                             if bone1 == 4 and bone2 == 1:
                                 print("* * * * *     * * * * *")
                                 print("* @   @ *     *       *")
                                 print("*       *     *   @   *")
                                 print("* @   @ *     *       *")
                                 print("* * * * *     * * * * *")
                             if bone1 == 4 and bone2 == 2:
                                 print("* * * * *     * * * * *")
                                 print("* @   @ *     *     @ *")
                                 print("*       *     *       *")
                                 print("* @   @ *     * @     *")
                                 print("* * * * *     * * * * *")
                             if bone1 == 4 and bone2 == 3:
                                 print("* * * * *     * * * * *")
                                 print("* @   @ *     *     @ *")
                                 print("*       *     *   @   *")
                                 print("* @   @ *     * @     *")
                                 print("* * * * *     * * * * *")
                             if bone1 == 4 and bone2 == 4:
                                 print("* * * * *     * * * * *")
                                 print("* @   @ *     * @   @ *")
                                 print("*       *     *       *")
                                 print("* @   @ *     * @   @ *")
                                 print("* * * * *     * * * * *")
                             if bone1 == 4 and bone2 == 5:
                                 print("* * * * *     * * * * *")
                                 print("* @   @ *     * @   @ *")
                                 print("*       *     *   @   *")
                                 print("* @   @ *     * @   @ *")
                                 print("* * * * *     * * * * *")
                             if bone1 == 4 and bone2 == 6:
                                 print("* * * * *     * * * * *")
                                 print("* @   @ *     * @   @ *")
                                 print("*       *     * @   @ *")
                                 print("* @   @ *     * @   @ *")
                                 print("* * * * *     * * * * *")
                             if bone1 == 5 and bone2 == 1:
                                 print("* * * * *     * * * * *")
                                 print("* @   @ *     *       *")
                                 print("*   @   *     *   @   *")
                                 print("* @   @ *     *       *")
                                 print("* * * * *     * * * * *")
                             if bone1 == 5 and bone2 == 2:
                                 print("* * * * *     * * * * *")
                                 print("* @   @ *     *     @ *")
                                 print("*   @   *     *       *")
                                 print("* @   @ *     * @     *")
                                 print("* * * * *     * * * * *")
                             if bone1 == 5 and bone2 == 3:
                                 print("* * * * *     * * * * *")
                                 print("* @   @ *     *     @ *")
                                 print("*   @   *     *   @   *")
                                 print("* @   @ *     * @     *")
                                 print("* * * * *     * * * * *")
                             if bone1 == 5 and bone2 == 4:
                                 print("* * * * *     * * * * *")
                                 print("* @   @ *     * @   @ *")
                                 print("*   @   *     *       *")
                                 print("* @   @ *     * @   @ *")
                                 print("* * * * *     * * * * *")
                             if bone1 == 5 and bone2 == 5:
                                 print("* * * * *     * * * * *")
                                 print("* @   @ *     * @   @ *")
                                 print("*   @   *     *   @   *")
                                 print("* @   @ *     * @   @ *")
                                 print("* * * * *     * * * * *")
                             if bone1 == 5 and bone2 == 6:
                                 print("* * * * *     * * * * *")
                                 print("* @   @ *     * @   @ *")
                                 print("*   @   *     * @   @ *")
                                 print("* @   @ *     * @   @ *")
                                 print("* * * * *     * * * * *")
                             if bone1 == 6 and bone2 == 1:
                                 print("* * * * *     * * * * *")
                                 print("* @   @ *     *       *")
                                 print("* @   @ *     *   @   *")
                                 print("* @   @ *     *       *")
                                 print("* * * * *     * * * * *")
                             if bone1 == 6 and bone2 == 2:
                                 print("* * * * *     * * * * *")
                                 print("* @   @ *     *     @ *")
                                 print("* @   @ *     *       *")
                                 print("* @   @ *     * @     *")
                                 print("* * * * *     * * * * *")
                             if bone1 == 6 and bone2 == 3:
                                 print("* * * * *     * * * * *")
                                 print("* @   @ *     *     @ *")
                                 print("* @   @ *     *   @   *")
                                 print("* @   @ *     * @     *")
                                 print("* * * * *     * * * * *")
                             if bone1 == 6 and bone2 == 4:
                                 print("* * * * *     * * * * *")
                                 print("* @   @ *     * @   @ *")
                                 print("* @   @ *     *       *")
                                 print("* @   @ *     * @   @ *")
                                 print("* * * * *     * * * * *")
                             if bone1 == 6 and bone2 == 5:
                                 print("* * * * *     * * * * *")
                                 print("* @   @ *     * @   @ *")
                                 print("* @   @ *     *   @   *")
                                 print("* @   @ *     * @   @ *")
                                 print("* * * * *     * * * * *")
                             if bone1 == 6 and bone2 == 6:
                                 print("* * * * *     * * * * *")
                                 print("* @   @ *     * @   @ *")
                                 print("* @   @ *     * @   @ *")
                                 print("* @   @ *     * @   @ *")
                                 print("* * * * *     * * * * *")
                             if sum == int(eeend2):
                                 print("Молодец! Угадал")
                                 if chance2 == 1:
                                     print("Нифига ты монстр!")
                                     score2 = score2 + (int(bet2) * 2)
                                     print("Твой счет -", score2)
                                     print("Счет игрока №1 -", score1)

                                     break
                                 if chance2 == 2:
                                     score2 = score2 + (int(bet2) * 1.9)
                                     print("Твой счет -", score2)
                                     print("Счет игрока №1 -", score1)

                                     break
                                 if chance2 == 3:
                                     score2 = score2 + (int(bet2) * 1.8)
                                     print("Твой счет -", score2)
                                     print("Счет игрока №1 -", score1)

                                     break
                                 if chance2 == 4:
                                     score2 = score2 + (int(bet2) * 1.7)
                                     print("Твой счет -", score2)
                                     print("Счет игрока №1 -", score1)

                                     break
                                 if chance2 == 5:
                                     score2 = score2 + (int(bet2) * 1.6)
                                     print("Твой счет -", score2)
                                     print("Счет игрока №1 -", score1)

                                     break
                             else:
                                 print("Не угадал!")
                                 round2 = round2 + 1

                                 if chance2 == round2:
                                     print("Твои попытки закончились")
                                     score2 = score2 - int(bet2)
                                     print("Твой счет -", score2)
                                     print("Счет игрока №1 -", score1)
                                     break
                     nova = 1
                 if score1 < 1 and score2 > score1:
                     print("Игрок 1 проиграл")
                     sail = input("Нажмите клавишу для выхода в главное меню")
                     system("cls")
                     break
                 elif score2 < 1 and score1 > score2:
                     print("Игрок 2 проиграл")
                     sail = input("Нажмите клавишу для выхода в главное меню")
                     system("cls")
                     break


print("Давай досвиданья!")


