def solution(d, budget):
    answer = 0
    mer = 0
    d.sort()
    for i in d:
        mer += i
        if mer > budget:
            break
        answer += 1
    return answer


def solution2(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)

print(solution2([1,3,2,5,4],9))