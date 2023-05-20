# 다시 풀어볼 문제

def solution(polynomial):
    xnum = 0
    num = 0
    for c in polynomial.split(' + '):
        if c.isdigit():
            num += int(c)
        else:
            print(c[:-1])
            xnum = xnum + 1 if c == 'x' else xnum+int(c[:-1])
    if xnum == 0:
        return str(num)
    elif xnum == 1:
        return 'x + ' + str(num) if num!=0 else 'x'
    else:
        return f'{xnum}x + {num}' if num!=0 else f'{xnum}x'
    