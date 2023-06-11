def solution(s):
    answer = []
    words = s.split(' ')
    for i in words:
        chan = ''
        for j in range(len(i)):
            if j % 2 == 0:
                chan += i[j].upper()
            else:
                chan += i[j].lower()
        answer.append(chan)
    return ' '.join(answer)

def solution2(s):
    return ' '.join(''.join([c.upper() if i % 2 == 0 else c.lower() for i,c in enumerate(w)]) for w in s.split())

print(solution2("try hello world"))
