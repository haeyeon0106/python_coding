def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += (a[i]*b[i])
    return answer

# 다른 사람 풀이
def solution2(a,b):
    return sum([i*j for i,j in zip(a,b)])

print(solution2([1,2,3,4],[-3,-1,0,2]))

