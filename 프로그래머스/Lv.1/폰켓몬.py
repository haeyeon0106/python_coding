def solution(nums):
    answer = 0
    a = len(set(nums))
    N = len(nums) // 2
    if a <= N:
        answer = a
    else:
        answer = N
    return answer

