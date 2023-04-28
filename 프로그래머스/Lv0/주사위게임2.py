def solution(a, b, c):
    answer = 0
    if a!=b & b!=c & c!=a:
        answer = a+b+c
    elif a == b & b == c & c == a:
        answer = (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)
    else:
        answer = (a+b+c)*(a**2+b**2+c**2)
    return answer

print(solution(2,6,1))
print(solution(5,3,3))
print(solution(4,4,4))