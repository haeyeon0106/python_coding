def solution(n):
    answer = 0
    result = []
    while n//3 > 0:
        result.append(n%3)
        n = n // 3
    result.append(n)
    for i in range(len(result)-1,-1,-1):
        answer += result[len(result)-i-1]*3**i
    return answer

def solution2(n):
    temp = ''
    while n:
        temp += str(n%3)
        n = n//3
    answer = int(temp,3)
    return answer

def solution3(n):
    answer = 0
    result = []
    while n//3 > 0:
        result.append(n%3)
        n = n // 3
    result.append(n)
    result.reverse()
    for i in range(len(result)):
        answer += result[i]*3**i
    return answer

print(solution3(125))