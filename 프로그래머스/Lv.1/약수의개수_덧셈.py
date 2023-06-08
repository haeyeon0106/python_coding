def solution(left, right):
    answer = 0
    count = 0
    mea = []        # 약수를 넣을 리스트
    for i in range(left,right+1):
        for j in range(1,i+1):
            if i % j == 0:
                mea.append(j)
        count = len(mea)    # 해당 숫자의 약수의 개수를 구한다
        mea.clear()         # 다음 숫자를 위해 리스트 비우기
        if count % 2 == 0:  # 약수의 개수가 짝수이면
            answer += i     # 현재 숫자에 더하기
        else:               # 약수의 개수가 홀수이면
            answer -= i     # 현재 숫자에 빼기
    return answer

def solution2(left,right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5) == i**0.5:
            answer -= i
        else:
            answer += i
    return answer

print(solution2(13,17))