# 내 풀이
from collections import deque
def sosu(n):
    answer = 0
    if n == 1: return 0
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            answer += 1
    return 1 if answer == 1 else 0 
def solution(n, k):
    answer = 0
    queue = deque()
    while n >= k:
        queue.appendleft(str(n%k))
        n = n // k
    queue.appendleft(str(n))
    queue = list(filter(None, ''.join(queue).split('0')))

    answer = sum([sosu(int(q)) for q in queue])
    return answer

# 다른사람 풀이
def conv(n,k):
    s = ''
    while n > 0:
        s += str(n%k)
        n = n // k
    return s[::-1]
def isprime(n):
    if n <= 1: return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def solution3(n, k):
    answer = 0
    for n in conv(n,k).split('0'):
        if not n: continue
        if isprime(int(n)):
            answer += 1
    return answer
