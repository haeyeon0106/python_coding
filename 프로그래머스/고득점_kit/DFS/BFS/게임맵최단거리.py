from collections import deque
def solution(maps):
    N = len(maps)
    M = len(maps[0])
    # 방문 여부와 최단거리 저장
    visited = [[False]*M for _ in range(N)]
    dist = [[0]*M for _ in range(N)]
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    start = (0,0)
    target = (N-1,M-1)
    queue = deque([start])
    visited[start[0]][start[1]] = True
    
    while queue:
        x,y = queue.popleft()
        
        if (x,y) == target:
            return dict[x][y]
        
        for i in range(4):
            nx,ny = dx[i] + x, dy[i] + y
            
            # 맵의 범위를 벗어나지 않고 이동이 가능, 아직 방문하지 않음
            if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] == 1 and not visited[nx][ny]:
                # 다음 위치를 큐에 넣음
                queue.append((nx,ny))
                # 방문표시
                visited[nx][ny] = True
                # 최단거리 저장
                dict[nx][ny] = dict[x][y] + 1
    return -1


