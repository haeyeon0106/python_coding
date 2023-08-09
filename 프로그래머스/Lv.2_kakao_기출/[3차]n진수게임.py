# 다른 사람 풀이를 참고한 풀이
def convert(n,base):
    arr = '0123456789ABCDEF'
    q,r = divmod(n,base)
    if q == 0:
        return arr[r]
    else:
        return convert(q,base) + arr[r]
def solution(n, t, m, p):
    answer = ''
    r = ''
    for i in range(m*t):
        r += str(convert(i,n))
    # for i in range(p-1,m*t,m):
    #      answer += r[i]
    return r[p-1:t*m:m]

# 위의 코드를 변환해서 구현한 나의 풀이
def convert2(n,base):
    result = ''
    alpha = 'ABCDEF'
    if n == 0:
        return '0'
    while n > 0:
        reminder = n % base
        if reminder >= 10:
            result += alpha[reminder%10]
        else:
            result += str(reminder)
        n = n // base
    return result[::-1]
def solution2(n, t, m, p):
    answer = ''
    r = ''
    for i in range(m*t):
        r += str(convert(i,n))
    return r[p-1:t*m:m]

# 다른 사람 풀이
def solution3(n, t, m, p):
    data = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    
    result = '0'
    for i in range(1,m*t):
        temp = []
        while i > 0:
            temp.append(data[i%n])
            i = i // n
        result += ''.join(reversed(temp))
    return result[p-1:m*t:m]