def solution(n):
    answer = []
    i = 2
    while n > 1:
        if n % i == 0:
            n = n // i
            answer.append(i)
        else:
            i += 1 
    return sorted(list(set(answer)))

# 리스트 삽입 좀 더 간단하게
def solution2(n):
    answer = []
    i = 2
    while n > 1:
        if n % i == 0:
            n = n // i
            if i not in answer:
                answer.append(i)
        else:
            i += 1 
    return answer

print(solution2(420))