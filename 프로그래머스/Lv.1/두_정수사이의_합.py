def solution(a, b):
    answer = 0
    if a > b:
        for i in range(b,a+1):
            answer += i
    elif a < b:
        for i in range(a,b+1):
            answer += i
    else :answer = a
    return answer

# 좋아요 많이 받은 풀이
def solution2(a,b):
    if a > b:
        a,b = b,a
    answer = sum([i for i in range(a,b+1)])
    return answer

print(solution2(5,3))
        