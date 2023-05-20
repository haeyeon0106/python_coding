def solution(numbers):
    answer = 0
    li = []
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            mul = numbers[i]*numbers[j]
            li.append(mul)
    answer = max(li)
    return answer

# 다른 사람 풀이

def solution(numbers):
    numbers.sort()
    return max(numbers[0]*numbers[1],numbers[-2]*numbers[-1])