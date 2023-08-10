import math
def solution(fees, records):
    answer = []
    park_time = {}
    in_out = {}
    for i in records:
        time,carnum,iNo = i.split(' ')
        h,m = time.split(':')
        if iNo == 'IN':
            in_out[carnum] = int(h)*60 + int(m)
        elif iNo == 'OUT':
            if carnum not in park_time.keys():
                park_time[carnum] = (int(h)*60+int(m)) - in_out[carnum]
            else:
                park_time[carnum] += (int(h)*60+int(m)) - in_out[carnum]
            in_out[carnum] = -1
    for carnum,time in in_out.items():
        last_time = 23*60+59
        if time >= 0:
            if carnum not in park_time:
                park_time[carnum] = last_time - in_out[carnum]
            else:
                park_time[carnum] += last_time - in_out[carnum]
    park_time = sorted(park_time.items())

    for num,time in park_time:
        if time < fees[0]:
            answer.append(fees[1])
        else:
            money = fees[1]
            money += math.ceil((time-fees[0])/fees[2])*fees[3]
            answer.append(money)
    return answer