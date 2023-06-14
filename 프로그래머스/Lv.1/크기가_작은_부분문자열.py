def solution(t, p):
    answer = 0
    N = len(t) - len(p)
    for i in range(N+1):
        if int(t[i:i+len(p)]) <= int(p):
            answer += 1        
    return answer