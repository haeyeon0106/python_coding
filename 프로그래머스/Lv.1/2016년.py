from datetime import datetime, date
def solution(a, b):
    answer = ''
    days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    day = date(2016,a,b).weekday()
    print(day)
    return days[day]

def solution2(a, b):
    answer = ''
    monthsum = 0
    for i in range(1,a):
        if i in (1,3,5,7,8,10,12):
            monthsum += 31
        elif i in (4,6,9,11):
            monthsum += 30
        else:
            monthsum += 29
    daysum = monthsum + b
    if daysum % 7 == 0:
        answer = 'THU'
    elif daysum % 7 == 1:
        answer = 'FRI'
    elif daysum % 7 == 2:
        answer = 'SAT'
    elif daysum % 7 == 3:
        answer = 'SUN'
    elif daysum % 7 == 4:
        answer = 'MON'
    elif daysum % 7 == 5:
        answer = 'TUE'
    elif daysum % 7 == 6:
        answer = 'WED'
    return answer

print(solution(5,24))