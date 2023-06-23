# 통과했지만 시간이 좀 오래걸림
def solution(s):
    answer = []
    result = ''
    for idx,alpha in enumerate(s):
        if alpha not in result:
            answer.append(-1)
        else:
            for i,a in reversed(list(enumerate(result))):
                if a == alpha:
                    answer.append(idx-i)
                    break
        result+=alpha
    return answer

def solution2(s):
    answer = []
    positions = {}
    for idx,char in enumerate(s):
        if char in positions:
            answer.append(idx-positions[char])
        else:
            answer.append(-1)
        positions[char] = idx   # 여기서 해당 알파벳의 인덱스 값(value)가 최근에 삽입된 알파벳 인덱스 값으로 바뀜
    return answer

print(solution2("banana"))

