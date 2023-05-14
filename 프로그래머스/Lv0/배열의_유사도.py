def solution(s1, s2):
    answer = 0
    for i in s2:
        for j in s1:
            if i == j: answer+=1
    return answer

# 다른 사람 풀이
def solution2(s1,s2):
    return len(set(s1)&set(s2))

solution2(["a", "b", "c"],["com", "b", "d", "p", "c"])