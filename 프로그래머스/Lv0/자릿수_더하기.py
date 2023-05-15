def solution(n):
    answer = 0
    
    for i in str(n):
        answer += int(i)
    return answer

# 다른 사람 풀이
def solution2(n):
    return sum([int(i) for i in str(n)])

def solution3(n):
    return sum(map(int,list(str(n))))

print(solution3(1234))