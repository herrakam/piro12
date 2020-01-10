stations = {}

def calc_station_info():
    with open('station_list.txt', 'r',encoding='UTF8') as file:
        for line in file:
            if line.strip('\n') == '':
                continue
            line = line.strip('\n')
            name, lineList = line.split('(')
            name = name.strip()
            lineList = lineList.strip(')')
            lineList = lineList.split(',')

            stations.setdefault(name, lineList)


if __name__ == '__main__':
    calc_station_info()
    print(stations)
    print(stations.keys())
    print(len(stations))

    # 역리스트 출처
# https://kin.naver.com/qna/detail.nhn?d1id=8&dirId=812&docId=343232296&qb=7KeA7ZWY7LKgIOyXrSDrqqnroZ0=&enc=utf8&section=kin&rank=2&search_sort=0&spq=0