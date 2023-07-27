# 문제 해석
# 감소했다가 증가하거나 그냥 증가하는 경우의 수는 해당 안됨
# 만약 증가했다가 감소해도 해당되어 시간 계산 해야함

from collections import deque
def solution(prices):
    answer = []
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            if prices[i] > prices[j]:
                break
        answer.append(j-i)
    return answer


# === 다른 사람 풀이 ===
def solution2(prices):
    answer = [0] * len(prices)
    stack = []
    
    for i in range(len(prices)-1):
        while stack != [] and stack[-1][1] > prices[i]:
            past,_ = stack.pop()
            answer[past] = i - past    
        stack.append([i,prices[i]])
        
    for i,s in stack:
        answer[i] = len(prices) - i -1
    return answer

def solution3(prices):
    answer = []
    prices = deque(prices)

    while prices:
        c = prices.popleft()
        count = 0

        for i in prices:
            if c > i:
                count += 1
                break
            count += 1
        answer.append(count)
    return answer
