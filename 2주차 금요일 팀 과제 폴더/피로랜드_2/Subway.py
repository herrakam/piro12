
import random
from station import *



def user_input(station_name):
    linenum = input('{}(은/는) 몇호선일까요? (1 ~ 9 중에서 입력해주세요) : '.format(station_name)).strip()
    return linenum


def playSubwayGame():
    calc_station_info()
    success = 0
    for trynum in range(5):
        r = 0
        station_name = ''
        line_list = []
        while True:
            can = False
            station_name, line_list = random.choice(list(stations.items()))
            temp = ['1호선', '2호선', '3호선', '4호선', '5호선', '6호선', '7호선', '8호선', '9호선']
            for j in temp:
                if j in line_list:
                    can = True
                    break
            if can:
                break



        print(station_name)
        print(line_list)


        try:
            u_input = user_input(station_name)
        except:
            print('시간초과. 패배.')
            break

        if u_input + '호선' not in line_list:
            print('정답이 아닙니다. 패배.')
            break
        success += 1

    if success == 5:
        return True
    return False




if __name__ == '__main__':
    playSubwayGame()
