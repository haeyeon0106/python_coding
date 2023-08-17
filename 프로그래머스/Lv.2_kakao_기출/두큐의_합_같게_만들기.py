# 예시는 통과했지만 시간초과 되어 통과하지 못한 코드
from collections import deque
def solution(queue1, queue2):
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    q1,q2 = sum(queue1),sum(queue2)
    num = (q1 + q2) // 2 
    
    M = len(queue1) + len(queue2)
    count = 0
    
    for i in range(M+1):
        q1,q2 = sum(queue1),sum(queue2) 
        if q1 == num and q2 == num:
            return count
        if q1 > num:
            queue2.append(queue1.popleft())
            count += 1
        elif q2 > num: 
            queue1.append(queue2.popleft())
            count += 1
    return -1

# 11,28번 테스트케이스 시간초과
def solution2(queue1, queue2):
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    q1_sum,q2_sum = sum(queue1),sum(queue2)
    num = (q1_sum + q2_sum) // 2 
    N = len(queue1)*len(queue2)
    count = 0
    
    while q1_sum != num:
        if count == N:
            return -1
        if q1_sum > num:
            n = queue1.popleft()
            queue2.append(n)
            q1_sum -= n
            q2_sum += n
            count += 1
        elif q2_sum > num:
            n = queue2.popleft()
            queue1.append(n)
            q2_sum -= n
            q1_sum += n
            count += 1
    return count

# 드디어 통과한 코드
def solution3(queue1, queue2):
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    q1_sum,q2_sum = sum(queue1),sum(queue2)
    num = (q1_sum + q2_sum) // 2 
    N = len(queue1)*4
    count = 0
    
    while q1_sum != num:
        if count == N:
            return -1
        if q1_sum > num:
            n = queue1.popleft()
            queue2.append(n)
            q1_sum -= n
            q2_sum += n
            count += 1
        elif q2_sum > num:
            n = queue2.popleft()
            queue1.append(n)
            q2_sum -= n
            q1_sum += n
            count += 1
    return count