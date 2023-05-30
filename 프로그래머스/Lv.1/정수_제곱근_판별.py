def solution(n):
    a = n**0.5
    if a.is_integer():
        return (a+1)**2
    else :
        return -1
    
# 다른 풀이
import math

def solution(n):
    a = math.sqrt(n)
    if a.is_integer():
        return (a+1)**2
    else :
        return -1