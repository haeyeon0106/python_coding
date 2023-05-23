
# 최대공약수를 구한 뒤 분모를 최대공약수로 나눈다
# 문제에서 기약분수로 나타내었을 때, 분모의 소인수가 2와 5만 존재해야 합니다. 이 부분을 잊지 말자
# 2와 5로 계속 나누어 b의 몫이 1일 때까지 while문을 사용하여 나눈다
import math
def solution(a, b):
    num = math.gcd(a,b)
    b = b//num
    while b % 2 == 0:
        b //= 2
    while b % 5 == 0:
        b //= 5
        
    return 1 if b == 1 else 2