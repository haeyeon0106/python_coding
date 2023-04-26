def solution(str1, str2):
    answer = ''
    
    l1 = list(str1)
    l2= list(str2)
    
    for i in range(len(l1)):
        answer += l1[i] + l2[i]

    return answer

print(solution('aaaaa','bbbbb'))