def solution(number, n, m):
    answer = 1 if number % n == 0 and number % m == 0 else 0
    return answer

print(solution(60,2,3))
print(solution(55,5,10))