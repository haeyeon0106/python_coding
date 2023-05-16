def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n == (i**2):
            answer = 1
            break
        else:
             answer = 2
    return answer

# 다른 사람 풀이

def solution2(n):
    return 1 if (n**0.5).is_integer() else 2        

# is_integer()은 정수인지 아닌지 판별
# 정수 n에 0.5승(즉 루트2)를 했을 때 정수이면 제곱수가 존재하고 정수가 아니면 제곱수가 존재하지 않는다.

print(solution2(144))