def solution(n):
    answer = 0
    for i in range(1,n+1):
        count = 0
        for j in range(1,i+1):
            if i % j == 0:
                count += 1
        if count > 2 : answer += 1
    return answer

# 다른 사람 풀이
def solution2(n):
    answer = 0
    for i in range(4,n+1):
        for j in range(2,int(i**0.5)+1):
            if i % j == 0:
                answer+=1
    return answer

print(solution2(10))