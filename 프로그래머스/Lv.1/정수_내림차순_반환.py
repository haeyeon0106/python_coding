# 문자열로 된 숫자도 정렬하면 오름차순/내림차순으로 정렬이 된다
def solution(n):
    answer = 0
    num = list(str(n))
    a = sorted([int(i) for i in num],reverse=True)
    return int(''.join(map(str,a)))

# 조금 더 간결하게
def solution(n):
    num = list(str(n))
    num.sort(reverse=True)
    return int(''.join(num))