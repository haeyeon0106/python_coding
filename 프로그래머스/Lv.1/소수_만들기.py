from itertools import combinations
def solution(nums):
    answer = 0
    remain = []
    for i in combinations(nums,3):
        for j in range(1,sum(i)+1):
            if sum(i) % j == 0:
                remain.append(j)
        if len(remain) == 2:
            answer += 1
        remain.clear()  
    return answer

def prime_number(x):
    answer = 0
    for i in range(1,int(x**0.5)+1):
        if x % i == 0:
            answer += 1
    return 1 if answer == 1 else 0
def solution2(nums):
    return sum([prime_number(sum(c)) for c in combinations(nums,3)])