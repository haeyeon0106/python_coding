def solution(n):
    answer = 0
    for i in range(max(n,6),6*n+1):
        if i % n == 0 and i % 6 == 0:
            answer = i // 6
            break
    return answer

print(solution(6))
print(solution(10))
print(solution(4))