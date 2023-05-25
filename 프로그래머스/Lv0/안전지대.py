def solution(board):
    
    N = len(board)
    # 상하좌우대각선(총 8개)를 x값,y값 나눠서 담아준다
    dx = [-1,1,0,0,-1,-1,1,1]
    dy = [0,0,-1,1,-1,1,-1,1]
    
    # 지뢰 설치
    boom = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                boom.append((i,j))  # 지뢰 인덱스 담기
    
    # 지뢰 설치된 곳 주변에 지뢰 설치
    for x,y in boom:
        for i in range(8):
            nx = x + dx[i]  # 현재 지뢰의 x좌표에 상하좌우대각선으로 더해줌
            ny = y + dy[i]  # 현재 지뢰의 y좌표에 상하좌우대각선으로 더해줌
            if 0 <= nx < N and 0 <= ny < N:
                board[nx][ny]=1
    
    # 안전지대 세기
    count = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                count += 1
    return count