def solution(new_id):
    answer = ''
    mark = '~!@#$%^&*()=+[{]}:?,<>/'
    # 1,2단계
    for i in new_id:
        if i.isupper():
            i = i.lower()
        if i in mark and not i.isdigit() and not i.isalpha():
            i = '' 
        answer += i
    # 3단계
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4단계
    if len(answer)>0 and answer[0] == '.': answer = answer[1:] 
    if len(answer)>0 and answer[-1] == '.': answer = answer[:-1]
    # 5단계
    if len(answer) == 0: answer += 'a'
    print(len(answer))
    # 6단계
    if len(answer)>=16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    #7단계
    if len(answer) <= 2:
        answer += answer[-1]*(3-len(answer))
    print(answer)
    return answer