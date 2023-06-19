# 예시는 통과했지만 정확성 테스트 10과 효율성 통과 못한 코드
def sosu(n):
    answer = 0
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            answer += 1
    return 1 if answer == 1 else 0
def solution(n):
    return sum([sosu(i) for i in range(2,n+1)])

