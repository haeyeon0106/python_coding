def solution(n):
    # 7의 배수면 몫 / 그 외는 몫+1
    return n // 7 if n%7 == 0 else n//7 + 1