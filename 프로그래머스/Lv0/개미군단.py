def solution(hp):
    answer = 0
    fight = [5,3,1]
    for i in fight:
        answer += hp // i
        hp = hp % i
    return answer