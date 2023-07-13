def solution(brown,yellow):
    total = brown + yellow
    middle = []

    for i in range(3,total):
        if total % i == 0:
            middle.append(i)
    
    for i in range(len(middle)):
        h = middle[i]
        w = total//h
        if (w-2)*(h-2) == yellow:
            return [w,h]
        
# 간략화한 풀이
def solution2(brown,yellow):
    total = brown + yellow
    for h in range(3,int(total**0.5)+1):
        w = total // h
        if (w-2)*(h-2):
            return [w,h]
        
print(solution2(10,2))