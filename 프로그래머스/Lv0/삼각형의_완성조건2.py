def solution(sides):
    return len([i for i in range(max(sides)-min(sides)+1,max(sides)+1)]) + len([i for i in range(max(sides)+1,sum(sides))])

# 다른 사람 풀이

# 1. 나머지 한 변의 길이가 제일 긴 경우(a > b)
# a < c < a + b
# 2. a의 길이가 제일 큰 경우
# a - b < c < a
# 종합 : a - b < c < a + b
# c의 개수 : (a+b)-(a-b)-1 = 2b-1 (b는 sides의 작은 수)
def solution2(sides):
    return 2*min(sides)-1

print(solution2([11, 7]))