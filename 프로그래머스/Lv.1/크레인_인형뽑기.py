def solution(board, moves):
    answer = 0
    basket = []
    for move in moves:
        for b in range(len(board)):
            if board[b][move-1] != 0: 
                doll = board[b][move-1]
                board[b][move-1] = 0
                
                if len(basket)>0 and basket[-1] == doll:
                    basket.pop()
                    answer += 2
                else:
                    basket.append(doll)
                break
    print(basket)
    return answer