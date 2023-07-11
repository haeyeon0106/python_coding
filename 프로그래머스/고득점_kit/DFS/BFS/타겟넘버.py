# ---- BFS ----
from collections import deque
def solution(numbers, target):
    answer = 0
    n = len(numbers)
    queue = deque([(0,0)])
    
    while queue:
        idx,total = queue.popleft()
        if idx == n:
            if total == target:
                answer += 1
            continue
        queue.append((idx+1,total+numbers[idx]))
        queue.append((idx+1,total-numbers[idx]))
    return answer

# ---- DFS ----
def solution2(numbers,target):
    answer = 0
    n = len(numbers)
    def dfs(idx,total):
        nonlocal answer
        if idx == n:
            if total == target:
                answer += 1
            return
        dfs(idx+1,total+numbers[idx])
        dfs(idx+1,total-numbers[idx])
    dfs(0,0)
    return answer
