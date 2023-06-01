def solution(s):
    answer = ''
    answer = sorted(s,reverse=True)
    return "".join(answer)

# 다른 사람 풀이
def solution2(s):
    s = list(s)
    s.sort(reverse=True)
    answer = ''
    for i in s:
        answer += i
    return answer

print(solution2("Zbcdefg"))