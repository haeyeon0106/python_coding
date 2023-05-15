def solution(n, numlist):
    answer = []
    for i in numlist:
        if i % n == 0:
            answer.append(i)
    return answer

# 다른 사람 풀이
def solution2(n,numlist):
    return list(filter(lambda i: i%n==0,numlist))

print(solution2(3,[4, 5, 6, 7, 8, 9, 10, 11, 12]))