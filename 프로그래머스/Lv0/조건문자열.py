def solution(ineq, eq, n, m):
    answer = 0
    if eq == "=":
        if ineq == "<" : answer = 1 if n <= m else 0
        elif ineq == ">" : answer = 1 if n >= m else 0
    elif eq == "!":
        if ineq == ">" : answer = 1 if n > m else 0
        elif ineq == "<" : answer = 1 if n < m else 0
    return answer


print(solution("<","=",20,50))
print(solution(">","!",41,78))