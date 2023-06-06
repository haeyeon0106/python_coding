def solution(s):
    num = '1234567890'
    if (len(s)==4) | (len(s)==6) and s.isdigit():
        return True
    return False

def solution2(s):
    try:
        int(s)
    except:
        return False
    return len(s) == 4 or len(s) == 6

print(solution2("a234"))
print(solution2("1234"))
