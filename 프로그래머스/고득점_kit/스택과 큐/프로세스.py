from collections import deque

# 통과하지 못한 나의 풀이..
def solution(priorities, location):
    answer = 0
    result = []
    
    for idx,val in enumerate(priorities):
        result.append([val,idx])
    result.sort(key=lambda x:(x[0],(x[0]-x[1])%6),reverse=True)
    for _,v in result:
        answer += 1
        if v == location:
            return answer
        


def solution2(priorities, location):
    answer = 0
    queue = deque([(p,i) for i,p in enumerate(priorities)])
    
    while queue:
        current = queue.popleft()
        if any(current[0] < q[0] for q in queue):
            queue.append(current)
        else:
            answer += 1
            if current[1] == location:
                return answer
        