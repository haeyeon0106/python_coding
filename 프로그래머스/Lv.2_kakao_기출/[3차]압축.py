# 내가 푼 코드
def solution(msg):
    answer = []
    alpha =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    result = ''
    for i in msg:
        result += i
        if result not in alpha:
            answer.append(alpha.index(result[:-1])+1)   # 현재 추가된 문자를 제외한 문자열 인덱스(색인) 추출
            alpha.append(result)            # 현재 문자열 사전에 추가
            result = result[-1]             
    answer.append(alpha.index(result)+1)
    return answer

# 다른 사람 코드를 참고하여 내 코드 수정
def solution2(msg):
    answer = []
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    dic = {k: v for (k, v) in zip(alpha, list(range(1, 27)))}

    result = ''
    for i in msg:
        result += i
        if result not in dic:
            dic[result] = len(dic) + 1  # 사전에 없는 단어를 사전에 추가
            result = result[:-1]  # 마지막 글자를 제외한 문자열을 사전에서 찾음
            answer.append(dic[result])
            result = i  # 현재 문자를 다시 초기화
    answer.append(dic[result])
    return answer

# 다른 사람 풀이
def solution3(msg):
    answer = []
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    d = {k: v for (k, v) in zip(alpha, list(range(1, 27)))}

    while True:
        if msg in d:
            answer.append(d[msg])
            break
        for i in range(1,len(msg)+1):
            if msg[0:i] not in d:
                answer.append(d[msg[0:i-1]])
                d[msg[0:i]] = len(d) + 1
                msg = msg[i-1:]
                break
    return answer
