def solution(a, b, flag):
    answer = (a+b) if flag == 1 else (a-b)
    return answer

print(solution(-4,7,True))