def solution(score):
    answer = []
    result=[]
    for i in score:
        result.append(sum(i))
    rank = sorted(result,reverse=True)
    
    for i in result:
        answer.append(rank.index(i)+1)
    return answer