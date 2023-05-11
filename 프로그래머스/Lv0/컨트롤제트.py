def solution(s):
    answer = 0
    s_list = s.split(" ")
    for key,value in enumerate(s_list):
        if value == 'Z':
            answer -= int(s_list[key-1])
        else:
            answer += int(value)
        
    return answer