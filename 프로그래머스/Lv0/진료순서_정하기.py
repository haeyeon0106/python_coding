def solution(emergency):
    answer=[]
    hurry = sorted(emergency,reverse=True)
    for i in emergency:
        answer.append(hurry.index(i)+1)
    return answer