def solution(slice, n):
    answer = 0
    # slice와 사람 수가 다르면 몫+1
    answer = n//slice if n % slice == 0 else n//slice+1
    return answer

print(solution(7,10))
print(solution(4,12))