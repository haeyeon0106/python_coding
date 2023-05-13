def solution(s):
    answer = ''
    for i in s:
        if s.count(i) == 1:
            answer+=i
    return "".join(sorted(answer))

# count() 함수 잊지말자!