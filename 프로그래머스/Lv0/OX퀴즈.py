def solution(quiz):
    answer = []
    for i in quiz:
        if eval(i.split('=')[0]) == int(i.split('=')[1]):
            answer.append('O')
        else:
            answer.append('X')
    return answer

# 다른 사람 풀이
def solution2(quiz):
    answer = []
    for i in quiz:
        L,R = i.split("=")
        a,op,b = L.split()
        if op == '+':
            answer += "O" if (int(a) + int(b)) == int(R) else "X"
        elif op == '-':
            answer += "O" if (int(a) - int(b)) == int(R) else "X"
    return answer
        


print(solution2(["3 - 4 = -3", "5 + 6 = 11"]))