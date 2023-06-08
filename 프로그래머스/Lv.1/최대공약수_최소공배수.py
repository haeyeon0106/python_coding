def solution(n, m):
    answer = []
    gcd = []
    lms = []
    for i in range(1,n+1):
        if n % i == 0 and m % i == 0:
            gcd.append(i)
    for i in range(m,n*m+1):
        if i % n == 0 and i % m == 0:
            lms.append(i)
    return [max(gcd),min(lms)]

def solution2(n, m):
    answer = []
    a,b = min(n,m),max(n,m)
    while a != 0:
        a,b = b%a,a
    answer = [b,int(n*m/b)]
    return answer
