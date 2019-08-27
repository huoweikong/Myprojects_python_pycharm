def fancy1():
    print('Hello Python world!\n')
    print('*' * 10)
    for i in range(5):
        print('*        *')
    print('*' * 10)
    print('*\n' * 6)

def fancy2():
    print("欢迎老道排序小王子：\n输入三个数，能够从小到大排列哦\n --->")
    l = []
    for i in range(3):
        x = int(input('integer:\n'))
        l.append(x)
    l.sort()
    print(l)

def fancy3():
    print('欢迎来到‘第几天’：\n输入年月日就能算出这是一年的第几天哦')
    year = int(input('year:\n'))
    month = int(input('month:\n'))
    day = int(input('day:\n'))

    months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
    if 0 <= month <= 12:
        sum = months[month - 1]
    else:
        print
        'data error'
    sum += day
    leap = 0
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        leap = 1
    if (leap == 1) and (month > 2):
        sum += 1
    print('it is the %dth day.' % sum)


if __name__ == '__main__':
    while True:
        logg = int(input('请输入数字1-3\n  --->'))
        if logg != 88:
            if logg == 1:
                fancy1()
            elif logg == 2:
                fancy2()
            elif logg == 3:
                fancy3()
            elif logg == 520:
                print("就知道你爱我")

        else:
            print("欢迎下次光临")
            break
