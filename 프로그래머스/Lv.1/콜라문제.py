# 예제 1번은 통과했지만 2번은 통과하지 못함(예저 당연히 통과 못함)
def solution(a, b, n):
    answer = 0
    while n >= 2:
        answer += n // a
        n = n//a + n%a
    return answer

# 예제 코드는 통과했지만 정확성은 통과하지 못함
def solution2(a, b, n):
    answer = 0
    for _ in range(n,0,-1):
        if n < 2:
            break
        answer += (n//a)
        n = (n//a) + (n%a)
    return answer

def solution3(a, b, n):
    answer = 0
    while n >= a:
        answer += (n//a)*b
        n = (n//a)*b + n%a
    return answer