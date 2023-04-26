# def solution(a, b):
#     if int(str(a) + str(b)) >= 2 * a * b : answer = int(str(a) + str(b))
#     else : answer = 2 * a * b
#     return answer

def solution(a, b):
    answer = max(int(str(a) + str(b)),2*a*b)
    return answer

print(solution(2,91))
print(solution(91,2))