import math
def solution(progresses, speeds):
    answer = []
    days = []

    for p,s in zip(progresses,speeds):
        d = math.ceil((100-p) / s)
        days.append(d)
    temp = days[0]
    count = 1

    for i in range(1,len(days)):
        if temp >= days[i]:
            count += 1
        else:
            temp = days[i]
            answer.append(count)
            count = 1
    answer.append(count)        
    return answer

# === 다른 사람 풀이 ===

def solution2(progresses, speeds):
    answer = []
    while(True):
        if len(progresses) > 0:
            check = 0
            for i in range(len(progresses)):
                progresses[i] = progresses[i] + speeds[i]
            print(progresses)
            if progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                check = check + 1
                while(True):
                    if len(progresses) <= 0 or progresses[0] < 100:
                        break
                    progresses.pop(0)
                    speeds.pop(0)
                    check = check + 1
                answer.append(check)
        else:
            break
    return answer

print(solution2([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))