import random
import turtle
import Subway
import time
import pickle
#승리, 패배시에 결과를 터틀로 출력하려고 했으나, 터틀 창이 한번 꺼진 뒤에
#다시 켜지지 않는 오류를 해결하지 못해서 일단 패스 ㅠㅠ


#캐릭터 클래스, 상태 출력하는 함수가 있음.
class Character:
    def __init__(self, name, money, coupon, victory, defeat):
        self.name = name
        self.money = money
        self.coupon = coupon
        self.victory = victory
        self.defeat = defeat

    def print_money_status(self):
        print("{}의 현재 가진 돈은 {}원입니다".format(self.name, self.money))

    def print_result_status(self):
        print("{}은 {}번 승리하였고, {}번 패배하였습니다.".format(self.name, self.victory, self.defeat))

    def print_coupon_status(self):
        print("{}이 가진 쿠폰은 수는 {}개입니니다.".format(self.name, self.coupon))

    def bankruptcy(self, player):
        if player.money <= 0:
            print('{}님이 파산하였습니다! 게임이 처음부터 진행됩니다'.format(player.name))
            me = Character(input('이름을 입력하세요:'), 10000, 0, 0, 0)


    # def money_charge(self,N): 쿠폰으로 돈 충전하는 기능, 아직 구현 못함



#게임 클래스, 한 판 할 때 마다 드는 비용으로 coin 이라는 클래스 속성 넣었고
# 베팅했을 때 어느 정도의 기댓값으로 돈을 딸 수 있는지에 대한 기대값 변수 넣음
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
    #패배시 캐릭터 인스턴스 변화 메소드
    def game_defeat(cls):
        me.defeat += 1
        cls.show_defeat_congrat()

    @classmethod
    #게임 시작시 재확인 하고 코인 쓰는 메소드
    def game_start(cls):
        a = int(input('게임을 시작하시겠습니까? 1(예), 2(아니오)  : '))
        if a == 1:
            me.money -= Game.coin
            cls.game_betting()
            pass
        elif a == 2:
            game_menu = print_game_menu()
        else:
            print('1 또는 2를 선택해주세요: ')
            cls.game_start()

    @classmethod
    # 게임 시작시 돈 거는 메소드
    def game_betting(cls):
        print("게임을 하려면 한판당 500원의 참가비가 소비됩니다.")
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

    @classmethod
    #승리시에 결과 출력하고 메뉴로 돌아가는 메소드(여기 원래 터틀을 넣었는데 ㅠㅠ)
    def show_victory_congrat(cls):
        print("\n승리!\n로딩중...\n")
        time.sleep(2)
        me.print_money_status()
        me.print_result_status()
        time.sleep(2)


    @classmethod
    #마찬가지로 패배시에 뜨고 메뉴로 돌아가기.
    def show_defeat_congrat(cls):
        print("\n패배!\n로딩중...\n")
        time.sleep(2)
        me.print_money_status()
        me.print_result_status()
        time.sleep(2)

    @classmethod
    #여기부터가 게임입니다! 저런식으로 표현을 했어요
    def dice(cls):
        t = turtle
        cls.game_start()
        a = int(input("주사위의 눈은 몇일까요?: "))
        if a == random.randrange(1, 7):
            cls.game_victory()
        else:
            cls.game_defeat()

    @classmethod
    def subway(cls):
        cls.game_start()
        if Subway.playSubwayGame():
            cls.game_victory()
        else:
            cls.game_defeat()

    @classmethod
    def baskinrobbins(cls):
        t = turtle
        print("게임플레이 방법\n 숫자 하나를 입력합니다.")
        print("1부터 시작하고,31을 입력하게 되면 패배하게 됩니다.")
        print("범위가 3~5일때, 4까지 입력하고 싶으면 4만 입력합니다.5까지 입력하고 싶으면 5만 입력합니다.")
        startnumber = 1
        cls.game_start()
        while (True):
            print("입력 가능한 숫자:%d~%d\n범위 밖의 숫자를 입력하면 탈락입니다." % (startnumber, startnumber + 2))
            a = int(input("숫자를 입력해주세요:"))
            print(a)
            show_warning = False
            if a < startnumber or a - 2 > startnumber:
                print("잘못 입력하셨습니다. 탈락!!!")
                break
            elif a >= 20 and show_warning == False:
                show_warning = True
                print("슬슬 머리써야 할 타이밍이에요 신중하게 입력하세요!!")
            startnumber = a + 1
            print("컴퓨터의 차례입니다.")
            b = random.randrange(startnumber + 1, startnumber + 3)
            if startnumber == 30:
                b = 31
            elif startnumber <= 29 and startnumber > 27:
                b = 30

            print(b)
            startnumber = b + 1
            if a >= 31:
                print("걸렸습니다!! 탈락!!!")
                cls.game_defeat()
                break
            if b >= 31:
                print("컴퓨터가 패배했습니다!! 축하합니다!!!")
                cls.game_victory()
                break

    @classmethod
    def generallee(cls):
        t = turtle
        print("100원짜리 동전 2개를 튕깁니다. 이순신 장군님 면이 한번에 나오면 패배입니다.")
        coin = ['이순신', '이순신', 100, 100]
        result=0
        cls.game_start()
        while True:
            print("당신의 차례입니다 동전을 튕깁니다.")
            print("던지기 강도를 선택해 주세요")
            print("숫자가 클수록 세게 던지게 됩니다.")
            print("세게 던지면 던질수록 결과가 느리게 나옵니다.")
            throw=int(input("[1,2,3,4,5]"))
            if throw==1:
                print("제일 약하게 튕깁니다.")
                print("틱")
                time.sleep(1)
            elif throw==2:
                print("약하게 튕깁니다. ")
                print("틱!!")
                time.sleep(2)
            elif throw==3:
                print("동전을 튕깁니다. ")
                print("팅!")
                time.sleep(2)
                print("빙글 빙글")
                time.sleep(1)
                print("틱!")
            elif throw==4:
                print("동전을 세게 튕깁니다.")
                print("티이잉!!!")
                time.sleep(3)
                print("빙그르르르....")
                time.sleep(2)
                print("틱!")
            else:
                print("동전을 매우 세게 튕깁니다. 거의 던지셨는데요...?")
                print("티이잉!!!!!!!!!!!!!!")
                time.sleep(4)
                print("빙그르르르르르르르르rrrrrrrrrrrrr")
                time.sleep(2)
                print("르르륵!")
            a=random.sample(coin,2)
            print(a)
            if a==['이순신','이순신']:
                print("두면 다 이순신이 나왔습니다.패배하였습니다!")
                print("시도한 횟수:%d" %result)
                cls.game_defeat()
                break
            else:
                print("다행히 장군님이 둘다 나오지 않았습니다.")
            result+=1
            print("상대의 차례입니다 동전을 튕깁니다.")
            print("팅!!")
            time.sleep(1)
            print("빙그르르르르.....")
            time.sleep(1)
            b=random.sample(coin,2)
            print(b)
            result += 1
            if b==['이순신','이순신']:
                print("상대가 던진 동전이 둘다 이순신이 나왔습니다 승리하였습니다!!")
                cls.game_victory()
                print("시도한 횟수:%d" % result)
                break
            else:
                print("다행히 장군님이 둘다 나오지 않았습니다.")




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
                return
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

    @classmethod
    def gugudan(cls):
        cls.game_start()
        print('\n구구단을 연속으로 12번 이상 맞추면 승리합니다! 3초안에 답해야되는 것도 알죠? >3<')
        print('\n구구단을 외자, 구구단을 외자~')
        time.sleep(3)
        print('시작!\n')
        lost = False
        for i in range(12):
            a = random.randrange(2, 9)
            b = random.randrange(1, 9)
            print(a, 'x', b, ':')
            start = time.time()
            answer = int(input())
            if time.time() - start > 3:
                print("박자는 생명! 박자는 생명!\n")
                lost = True
                break
            elif answer != a * b:
                print('구구단도 모르는 바보 자식~\n')
                lost = True
                break
        if lost == True:
            cls.game_defeat()
        else:
            cls.game_victory()

# 시작 메뉴 출력 함수
def print_menu():
    print()
    print("1. 상태 보기")
    print("2. 게임 하기")
    print("3. 종료")
    print()
    menu = input("메뉴선택: ")
    return int(menu)

#상태 보기 메뉴 출력 함수
def print_status_menu():
    print()
    print("1. 현재 남은 돈 보기")
    print("2. 게임 결과 보기")
    print("3. 보유 쿠폰 수 보기")
    print("4. 뒤로 가기")
    print()
    status_menu = input("메뉴선택: ")
    return int(status_menu)

#게임 하기 메뉴 출력 함수
def print_game_menu():
    print()
    print("1. 주사위 굴리기")
    print("2. 베스킨라빈스 ")
    print("3. 지하철 몇호선인지 5개 맞추기")
    print("4. 회문찾기")
    print("5. 구구단 게임")
    print("6. 이순신게임")
    print("10. 뒤로 가기")
    game_menu = input("메뉴선택: ")
    return int(game_menu)

#프로그램 시작시 첫 메뉴를 출력하는 함수

def run():
    while True:
        menu = print_menu()
        while menu == 1:
            status_menu = print_status_menu()
            while status_menu != 4:
                if status_menu == 1:
                    me.print_money_status()
                    status_menu = print_status_menu()
                elif status_menu == 2:
                    me.print_result_status()
                    status_menu = print_status_menu()
                elif status_menu == 3:
                    me.print_coupon_status()
                    status_menu = print_status_menu()
            if status_menu == 4:
                menu = print_menu()
        if menu == 2:
            game_menu = print_game_menu()
            if game_menu == 1:
                Game.dice()
            elif game_menu == 2:
                Game.baskinrobbins()
            elif game_menu == 3:
                Game.subway()
            elif game_menu == 4:
                Game.palinderome()
            elif game_menu == 5:
                Game.gugudan()
            elif game_menu == 6:
                Game.generallee()
            elif game_menu == 10:
                menu = print_menu()

        if menu == 3:
            print()
            break

def show_ranking():
    # user ranking 출력
    user_rank = []
    with open('users.p', 'rb') as f:
        while True:
            try:
                data = pickle.load(f)
                user_rank.append([data.money, data.name])
            except EOFError:
                break
    user_rank.sort(reverse=True)
    for i in range(len(user_rank)):
        print(i + 1, '등: ', user_rank[i][1], ' ', user_rank[i][0], '원', sep='')


if __name__ == '__main__':
    # user1 = Character('쫑인', 13000, 1, 15, 7)
    # user2 = Character('쑤현', 20000, 2, 20, 4)
    # user3 = Character('씅현', 11000, 3, 10, 5)
    # user4 = Character('째복', 5000, 4, 8, 15)
    # user_list2 = []
    # user_list2.append(user1)
    # user_list2.append(user2)
    # user_list2.append(user3)
    # user_list2.append(user4)
    # with open('users.p', 'wb') as f:
    #     for a in user_list2:
    #         pickle.dump(a, f)
    show_ranking()
    user_name = input('이름을 입력하세요: ')
    user_exist = False
    user_list = []
    with open('users.p', 'rb') as f:
        while True:
            try:
                data = pickle.load(f)
            except EOFError:
                break
            if data.name == user_name:
                me = data
                user_exist = True
            else:
                user_list.append(data)

    if not user_exist:
        me = Character(user_name, 10000, 0, 0, 0)

    run()

    user_list.append(me)
    with open('users.p', 'wb') as f:
        for a in user_list:
            pickle.dump(a, f)

    show_ranking()




# 캐릭터 파일 저장해서 읽고 쓰는 기능 있으면 좋겠는데 구현을 못했네요 ㅠㅠ
# 게임 클래스에는 패배시에 랜덤 쿠폰 지급이 존재하는 클래스 메소드를 넣을거에요!
# 쿠혼으로 돈 충전할 수 있는 메소드 넣을거에요!
# 게임을 마치고 난 뒤,  현재 정보 파일에 저장하기 가 아직 없습니다
# 승리시에 돈 변화하고 기댓값에 따라 배팅해서 돈 잃고 얻는거 아직 구현 안함
# 게임도 한개밖에 없음 ㅠㅠ
# 뭔가 로딩중 이러던가, 피로랜드에 오신걸 환영합니다! 같은 꾸미기가 있으면 재밌을 것 같은데 제가 아직 구현을....
# 늦게 참여해서 죄송합니다 ㅠㅠ