import random

from chart_generator import to_format

def generate_to_jump(il = 1):
    years = range(2018, 2023)
    months = range(1,13)
    hours = range(24)
    minutes = range(60//il)
    d28 = [2]
    d30 = [4,6,9,11]
    d31 = [1,3,5,7,8,10,12]

    for year in years:
        for month in months:
            if d28.__contains__(month):
                if year == 2020:
                    days = range(1,30)
                else:
                    days = range(1,29)
            elif d30.__contains__(month):
                days = range(1,31)
            elif d31.__contains__(month):
                days = range(1,32)

            for day in thanos(days):
                for hour in thanos(hours):
                    for m in thanos(minutes):
                        minute = m * il
                        yield to_format(year, month, day, hour, minute)

## 배열 일부 랜덤으로 짜르기
def thanos(arr):
    arr = list(arr)
    random.shuffle(arr)
    return arr[:len(arr)//4]

def main():
    count = 0
    interval_list = [3,5,10,15]
    for il in interval_list:
        for g in generate_to_jump(il):
            print(g)
            count += 1
    print(count)

if __name__ == "__main__":
    main()