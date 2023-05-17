def solution(my_str, n):
    answer = []
    for i in range(0,len(my_str),n):
        answer.append(my_str[i:i+n])
    return answer

# 다른 사람 풀이

# 내 풀이를 간략하게 표현하였다.
def solution2(my_str, n):
    return [my_str[i:i+n] for i in range(0,len(my_str),n)]

print(solution2("abc1Addfggg4556b",6))