def solution(dartResult):
    answer = 0
    score = []
    current = ''
    for char in dartResult:
        if char.isdigit():
            current += char
        elif char == 'S':
            score.append(int(current)**1)
            current = ''
        elif char == 'D':
            score.append(int(current)**2)
            current = ''
        elif char == 'T':
            score.append(int(current)**3)
            current = ''
        elif char == '*':
            if len(score) >= 2:     # *가 중첩일 경우
                score[-2] *= 2      # *가 두 개 중첩이면 4배, #와 중첩이면 2*(-1)
            score[-1] *= 2
        elif char == '#':
            score[-1] *= -1
    return sum(score)