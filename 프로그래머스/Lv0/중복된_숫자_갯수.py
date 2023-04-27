def solution(array, n):
    answer = 0
    for i in range(len(array)):
        if n == array[i] : answer += 1

    # 타인풀이 참고
    answer = array.count(n)
    return answer

print(solution([1, 1, 2, 3, 4, 5],1))
print(solution([0, 2, 3, 4],1))