def solution(my_string):
    answer = []
    for i in my_string:
        answer.append(i)
    answer.reverse()
    answer = "".join(answer)
    return answer

print(solution("jaron"))
print(solution("bread"))