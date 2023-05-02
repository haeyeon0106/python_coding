def solution(numer1, denom1, numer2, denom2):
    answer = []
    for i in range(max(denom1,denom2),denom1*denom2+1):
        if i % denom1 == 0 and i % denom2 == 0:
            numer = (i // denom1)*numer1 + (i//denom2)*numer2
            denom = i
            for i in range(denom+1,0,-1):
                if numer % i == 0 and denom%i == 0:
                    numer //= i
                    denom //= i
                    break
            answer.append(numer)
            answer.append(denom)
            break
    return answer

print(solution(1,2,3,4))
print(solution(9,2,1,3))
print(solution(4,4,4,4))