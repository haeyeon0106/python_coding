def solution(my_string):
    answer = []
    num = ["0","1","2","3","4","5","6","7","8","9"]
    for i in my_string:
        if i in num:
            answer.append(int(i))
    return sorted(answer)

# 다른 사람 풀이
def solution2(my_string):
    return sorted([int(i) for i in my_string if i.isdigit()])

print(solution2("hi12392"))