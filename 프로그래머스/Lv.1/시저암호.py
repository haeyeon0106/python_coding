def solution(s, n):
    answer = ''
    for c in s:
        if c.isalpha(): # 알파벳이라면
            if c.islower():   #소문자라면
                char = chr((ord(c)-ord('a')+n)%26 +ord('a'))
            else:
                char = chr((ord(c)-ord('A')+n)%26 +ord('A'))
        else:   # 빈칸이면 바로 대입
            char = c
        answer += char
    return answer

# 다른 사람 풀이
def solution(s, n):
    answer = ''
    low = "abcdefghijklmnopqrstuvwxyz" # 소문자. 인덱스는 0에서 25
    up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for char in s:
        if char in low:
            i = low.find(char) + n
            answer += low[i%26]
        elif char in up:
            i = up.find(char) + n
            answer += up[i%26]
        else:
            answer += char
    return answer