def solution(num, n):
    answer = 0
    answer = 1 if num % n == 0 else 0
    return answer

print(solution(98,2))
print(solution(34,3))