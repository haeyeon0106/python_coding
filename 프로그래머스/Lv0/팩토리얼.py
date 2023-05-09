from math import factorial

def solution(n):
    i = 0
    while True:
        if factorial(i) > n:
            break
        i+=1
    return (i-1)

# 제한사항
# 0 < n ≤ 3,628,800(10!)

# 다른 사람 풀이
def solution2(n):
    k = 10      # 제한사항에 n의 최댓값이 3,628,800(10!)이기 때문에 factorial(k)에서 k의 최댓값은 10
    while n < factorial(k):
        k -= 1
    return k

print(solution2(3628800))