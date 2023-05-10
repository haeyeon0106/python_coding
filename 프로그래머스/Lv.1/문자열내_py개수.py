def solution(s):
    p = 0
    y = 0
    for i in s:
        if i == 'p' or i == 'P':
            p += 1
        elif i == 'y' or i == 'Y':
            y += 1
    if p == y : 
        return True
    else:
        return False
    
# 다른 사람 풀이
def solution2(s):
    return s.lower().count('p') == s.lower().count('y')

print(solution2("pPoooyY"))