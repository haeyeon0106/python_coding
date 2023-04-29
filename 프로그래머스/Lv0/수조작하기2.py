def solution(numLog):
    answer = ''
    for i in range(len(numLog)):
        if i == len(numLog)-1 : break
        num = numLog[i+1]-numLog[i]
        
        if num== 1 : answer+='w'
        elif num==-1 : answer +='s'
        elif num==10 : answer += 'd'
        else : answer += 'a'
    return answer