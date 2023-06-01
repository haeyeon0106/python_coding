def solution(s):
    answer = ''
    re = len(s)//2
    answer = s[re-1]+s[re] if len(s) % 2 == 0 else s[re]
    return answer

# 다른 사람 풀이
def string_middle(str):
    a = len(str)
    if a % 2 == 0 :
        a = (a-2) / 2
    else :
        a = (a-1) / 2
    return str[int(a) : -int(a)]