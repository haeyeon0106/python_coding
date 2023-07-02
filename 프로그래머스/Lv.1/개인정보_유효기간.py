def solution(today, terms, privacies):
    answer = []
    term = {}
    to = list(map(int,today.split('.')))
    
    for t in terms:
        term[t.split()[0]] = int(t.split()[1])
    for idx,privacy in enumerate(privacies): 
        p = list(map(int,privacy.split()[0].split('.')))
        # 유효기간 month 수정
        p[1] += term[privacy.split()[1]]
        # day 1씩 빼기
        p[2] -= 1
        
        # month가 12를 넘었을 때
        while p[1] > 12:
            p[1] -= 12
            p[0] += 1
        # if p[2] == 0:
        #     p[1] -= 1
        #     p[2] = 28
        #     if p[1] == 0:
        #         p[0] -= 1
        #         p[1] = 12
        
        if p[0] > to[0] :
            continue    
        elif p[0] == to[0] :
            if p[1] > to[1] :
                continue   
            elif p[1] == to[1] :
                if p[2] >= to[2] :
                    continue
        answer.append(idx + 1)
    return answer
