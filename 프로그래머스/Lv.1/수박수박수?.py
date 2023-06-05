def solution(n):
    answer = '수'
    for i in range(1,n):
        if answer[i-1] == '수':
            answer += '박'
        elif answer[i-1] == '박':
            answer += '수'
    return answer

# 다른 사람 풀이
def solution2(n):
    str = "수박"*n
    return str[:n]

def solution3(n):
    answer = ''
    for i in range(n):
        if i % 2 == 0:
            answer += '수'
        else:
            answer += '박'
    return answer

print(solution3(3))