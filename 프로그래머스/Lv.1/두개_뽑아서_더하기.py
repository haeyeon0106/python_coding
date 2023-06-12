from itertools import combinations
def solution(numbers):
    answer = []
    answer = list(map(sum,list(combinations(numbers,2))))
    answer = sorted(set(answer))
    return answer

def solution2(numbers):
    answer = []
    for i in combinations(numbers,2):
        answer.append(sum(i))
    answer = sorted(set(answer))
    return answer

def solution3(numbers):
    answer = []
    for i in range(0,len(numbers)-1):
        for j in range(i+1,len(numbers)):
            answer.append(numbers[i]+numbers[j])
    answer = sorted(set(answer))
    return answer

print(solution3([2,1,3,4,1]))