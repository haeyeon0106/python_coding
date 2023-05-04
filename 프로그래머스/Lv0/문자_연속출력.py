def solution(my_string, n):
    answer = []
    for i in my_string:
        answer+=(i*3)
    answer = "".join(answer)
    return answer
# def solution(my_string, n):
#     return "".join(s*n for s in my_string)

print(solution("hello",3))
print(solution("HELLO",3))