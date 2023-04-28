def solution(n):
    answer = []
    answer.append(n)
    while True:
        if n == 1: break
        if n % 2 == 0 :
            n = n / 2
        elif n % 2 == 1:
            n = 3*n+1
        answer.append(int(n))
    return answer

print(solution(10))