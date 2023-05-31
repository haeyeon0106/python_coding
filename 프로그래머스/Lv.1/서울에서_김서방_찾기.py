def solution(seoul):
    num = 0
    for i in range(len(seoul)):
        if 'Kim' == seoul[i]:
            num = i
    answer = "김서방은 " + str(num)+"에 있다"
    return answer

# 다른 사람 풀이
def solution2(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))