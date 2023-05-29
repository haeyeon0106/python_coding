# 처음에 common 마지막 수를 max(common)으로 설정하였다
# 테스트 8에 막혀 힌트를 참고하였다.
# 공비가 마이너스일 경우를 대비하여 max를 사용하면 안됨
# 따라서 배열 마지막 수를 common[-1]로 설정
def solution(common):
    answer = 0
    if common[1]-common[0] == common[2]-common[1]:
        answer = common[-1]+(common[1]-common[0])
    elif common[1]//common[0] == common[2]//common[1]:
        answer = common[-1]*(common[1]//common[0])
    return answer

# 다른 사람 풀이
def solution2(common):
    # 뒤에서 숫자 세 개 추출
    a,b,c = common[:3]
    if (b-a) == (c-b):
        return common[-1]+(b-a)
    elif (b//a) == (c//b):
        return common[-1]*(b//a)