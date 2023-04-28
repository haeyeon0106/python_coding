from functools import reduce
def solution(num_list):
    answer = 0
    total = sum(num_list)
    multiple = reduce(lambda x,y:x*y,num_list)
    if multiple < total**2:
        answer = 1
    return answer

print(solution([3, 4, 5, 2, 1]))
print(solution([5, 7, 8, 3]))