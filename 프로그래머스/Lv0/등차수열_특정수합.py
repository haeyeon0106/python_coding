def solution(a, d, included):
    list1 = []
    for i in range(len(included)):
        if included[i] == True:
            list1.append(d*i+a)
    answer = sum(list1)
    return answer



print(solution(3,4,[True, False, False, True, True]))
