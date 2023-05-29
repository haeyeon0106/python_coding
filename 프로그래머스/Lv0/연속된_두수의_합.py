# 아직 원리파악을 못했다... 넘 어려워...

def solution(num, total):
    answer = []
    average = total // num
    answer = [i for i in range(average - (num-1)//2, average + (num+2)//2)]
    return answer