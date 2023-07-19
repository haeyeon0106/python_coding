from itertools import permutations
def solution(k, dungeons):
    answer = 0
    l = len(dungeons)
    for o in permutations(range(l)):
        tk = k
        for n,i in enumerate(o):
            if tk < dungeons[i][0]:
                answer = max(answer,n)
                break
            tk -= dungeons[i][1]
        else:
            return l
    print(answer)
    return answer

# 다른 사람 풀이
answer = 0
N = 0
visited = []


def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt

    for j in range(N):
        if k >= dungeons[j][0] and not visited[j]:
            visited[j] = 1
            dfs(k - dungeons[j][1], cnt + 1, dungeons)
            visited[j] = 0


def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0, dungeons)
    return answer