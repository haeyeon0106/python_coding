from itertools import combinations
def solution(clothes): 
    cloth = {}
    result = []
    for i in range(len(clothes)):
        name,kind = clothes[i]
        if kind not in cloth:
            cloth[kind] = []
        cloth[kind].append(name)
    
    for key in cloth.keys():
        result.append(len(cloth[key]))
    answer = 1
    
    # 의상의 조합 수 계산
    for r in result:
        answer *= (r+1)
    return answer-1     # 모든 의상을 입지 않는 경우 1을 빼줌
        
def solution2(clothes):
    cloth ={}
    for _,kind in clothes:
        if kind not in cloth:
            cloth[kind] = 2
        else:
            cloth[kind] += 1
    cnt = 1
    for num in cloth.values():
        cnt *= num
    return cnt-1
