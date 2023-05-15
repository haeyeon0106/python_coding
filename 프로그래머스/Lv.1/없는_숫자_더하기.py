def solution(numbers):
    answer = 0
    for i in range(0,10):
        if i not in numbers:
            answer += i
    return answer

# 좋아요 많이 받은 풀이
def solution2(n):
    return 45 - sum(n)

solution3 = lambda x : sum(range(10)) - sum(x)

print(solution2([1,2,3,4,6,7,8,0]))
print(solution3([1,2,3,4,6,7,8,0]))
