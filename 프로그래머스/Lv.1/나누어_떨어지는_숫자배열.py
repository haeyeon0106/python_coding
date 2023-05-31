def solution(arr, divisor):
    answer = sorted([i for i in arr if i % divisor == 0])
    if len(answer)==0: answer.append(-1)
    return answer

def solution2(arr,divisor):
    return sorted([i for i in arr if i % divisor == 0]) or [-1]

print(solution2([5, 9, 7, 10],5))