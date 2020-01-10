class Game:
    coin = 500
    expectation = 1.1
    betting = 0

    @classmethod
    #승리시 캐릭터 인스턴스 변화 메소드
    def game_victory(cls):
        me.victory += 1
        print(Game.betting)
        me.money += Game.betting * 2
        cls.show_victory_congrat()

    @classmethod
    # 게임 시작시 돈 거는 메소드
    def game_betting(cls):
        Game.betting = int(input('얼마를 베팅하시겠습니까? 한 판 금액의 2배까지 가능합니다.:  '))
        if Game.betting % 100 != 0:
            print('100원 단위로 입력해주세요')
            cls.game_betting()
        elif Game.betting % 100 == 0:
            if Game.betting > Game.coin * 3:
                print('2배 초과는 베팅할 수 없습니다.')
                cls.game_betting()
            else:
                me.money -= Game.betting
        else:
            print('숫자를 입력해주세요')
            cls.game_betting()


    #새로운 게임!
    @classmethod
    def palinderome(cls):
        cls.game_start()
        palindromelist = (['anna'], ['civic'], ['kayak'], ['level'], ['madam', 'mom'], ['noon'],
                          ['racecar', 'radar', 'redder', 'refer', 'repaper'
                              , 'rotator', 'rotor'], ['sagas', 'solos', 'stats'], ['tenet'], ['wow'])

        problemset = []
        answerset = []
        point = 0
        comppoint = random.randrange(1, 4) * 100
        a = 0

        for wordbag in range(3):
            wordbag = palindromelist[random.randrange(1, len(palindromelist))]
            if len(wordbag) == 1:
                problemset.append(wordbag[0])
                answerset.append(wordbag[0])
            elif len(wordbag) >= 2:
                problemset.append(wordbag[random.randrange(1, len(wordbag))])
                answerset.append(wordbag)

        while True:
            print("게임을 시작합니다. 이 게임은 빠른 시간 안에 컴퓨터보다 빠르게 회문 단어를 찾는 게임입니다.")
            time.sleep(1)
            a = int(input('머리속으로 회문 단어를 생각하세요. 시작할 준비가 되셨나요? 1(예), 2(아니오): '))
            if a != 1:
                print("처음으로 돌아갑니다! 돈은 돌려드리겠습니다.")
                time.sleep(3)
                me.money += 500
                Game.palindrome
            elif a == 1:
                for i in range(3):
                    print('{}번째 문제입니다. 이 단어는 {}로 시작하는 {}글자 단어입니다'.format(i + 1, problemset[i][0], len(problemset[i])))
                    while True:
                        answer = input().lower()
                        if answer in answerset[i]:
                            print('정답!')
                            point += 100
                            break
                        elif answer == '?':
                            print('다음 문제로 넘어갑니다.')
                            time.sleep(1.5)
                            break
                        else:
                            print('정답이 아닙니다. 다시 시도하세요. 모르겠으면 ? 를 입력하세요')

            print("수고하셨습니다! 당신의 최종 점수는 {} 입니다.".format(point))
            time.sleep(1)
            print("컴퓨터의 점수는 {}입니다.".format(comppoint))
            time.sleep(1)
            if point > comppoint:
                print('당신이 승리하셨습니다')
                a += 1
                break
            elif point == comppoint:
                print('비겼지만 이긴거로 해드리죠!')
                a += 1
                break
            else:
                print('컴퓨터한테 졌습니다. 분발하세요')
                break

        if a == 0:
            cls.game_defeat()
        else:
            cls.game_victory()