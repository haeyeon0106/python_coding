def solution(l, r):
    result = []
    for num in range(l, r+1):
        if set(str(num)) <= set('05'):
            result.append(num)
    return result if result else [-1]