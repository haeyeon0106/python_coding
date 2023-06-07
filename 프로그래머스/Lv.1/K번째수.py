def solution(array, commands):
    answer = []
    for i,j,k in commands:
        a = sorted(array[i-1:j])[k-1]
        answer.append(a)
    return answer

# 다른 사람 풀이
def solution2(array,commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1],commands))

print(solution2([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))