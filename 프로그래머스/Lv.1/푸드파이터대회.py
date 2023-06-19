from collections import deque
def solution(food):
    answer = []
    a = deque(answer)
    a.append(0)
    for i,num in reversed(list(enumerate(food))):
        for _ in range(num//2):
            a.append(i)
            a.appendleft(i)
    return ''.join(list(map(str,a)))

def solution2(food):
    first = ''.join(str(num)*(quan//2) for num,quan in enumerate(food))
    second = first[::-1]
    answer = first + '0' + second
    return answer

print(solution2([1,3,4,6]))