def solution(n, t):
    for i in range(1,t+1):
        n = n*2
    return n

# 다른 사람 풀이

# 좋아요 많이 받은 풀이는 비트연산자를 사용하였지만
# 비트연산자는 익숙하지 않아서 다른 풀이를 공부하였다.

def solution2(n, t):
    return (2**t)*n