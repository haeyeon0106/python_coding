from collections import Counter
def jarkard(str3):
    result = []
    string = ''
    for i in str3:
        if i.isalpha():
            string += i
        elif i == ' ' or not i.isalpha():
            string = ''
        if len(string) == 2:
            result.append(string)
            string = string[-1]
    return result
    
def solution(str1, str2):
    A = jarkard(str1.upper())
    B = jarkard(str2.upper())
    
    # 합집합
    union = Counter(A) | Counter(B)
    # 교집합
    intersection = Counter(A) & Counter(B)
    
    if len(union) == 0 and len(intersection) == 0:
        j = 1
    else:
        j = sum(intersection.values()) / sum(union.values())
    
    return int(j*65536)