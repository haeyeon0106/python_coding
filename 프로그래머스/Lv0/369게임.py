def solution(order):
    answer = 0 
    num_list = list(str(order))
    for i in num_list:
        if int(i) == 0: continue
        if int(i) % 3 == 0:
            answer += 1
    return answer