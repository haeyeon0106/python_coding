def solution(balls, share): 
    return factorial(balls) / (factorial(balls-share) * factorial(share))

def factorial(n):
    if n>1 : return n * factorial(n-1)
    else : return 1