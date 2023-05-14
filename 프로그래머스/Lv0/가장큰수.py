def solution(array):
    answer = []
    a = max(array)
    b = array.index(a)
    answer.append(a)
    answer.append(b)
    return answer

# 다른 사람 풀이
def solution2(array):
    return [max(array),array.index(max(array))]

print(solution2([1, 8, 3]))