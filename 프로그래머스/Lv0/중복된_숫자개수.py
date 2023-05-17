def solution(array, n):
    answer = 0
    for i in range(len(array)):
        if n == array[i] : answer += 1
    return answer

# 다른 사람 풀이
def solution2(array,n):
    return array.count(n)
