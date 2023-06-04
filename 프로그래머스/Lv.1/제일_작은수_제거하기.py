def solution(arr):
    arr.remove(min(arr))
    return [-1] if len(arr) == 0 else arr

# 다른 사람 풀이
def solution2(arr):
    return [i for i in arr if i > min(arr)]

print(solution2([4,3,2,1]))