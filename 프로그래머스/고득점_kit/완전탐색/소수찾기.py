from itertools import permutations
def verify(num):
    if num == 0 or num == 1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False     # 소수가 아님
    return True            # 소수임

def solution(numbers):
    answer = 0
    nums = list(map(str,numbers))
    result = []
    for i in range(1,len(nums)+1):
        for j in permutations(nums,i):  # 17과 71의 순서가 중요하기 때문에 조합이 아닌 순열
            result.append(int(''.join(j)))
    # result = sorted(list(set(result)))

    for i in list(set(result)):
        if verify(i):
            answer += 1
    return answer

from itertools import permutations
def decimal(num):
    count = 0
    if num == 0 or num == 1:
        return 0
    for i in range(2,int(num*0.5)+1):
        if num % i == 0:
            return 0
    return 1
def solution2(numbers):
    answer = 0
    numbers = list(numbers)
    result = []
    total = []
    for i in range(1,len(numbers)+1):
        for j in permutations(numbers,i):
            result.append(int(''.join(j)))

    for i in set(result):
        n = decimal(i)
        total.append(n)
        
    return sum(total)