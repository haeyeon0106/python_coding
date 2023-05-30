# 통과하지 못한 나의 풀이...ㅠ
# def solution(n, lost, reserve):
#     answer = 0
#     physical = []
#     lost.sort()
#     reserve.sort()
#     for i in range(n):
#         physical.append(i+1)
#         for j in lost:
#             if (i+1) == j:
#                 physical.remove(j)
#     for i in range(len(reserve)):
#         for j in lost:
#             if (reserve[i]-1) == j or (reserve[i]+1) == j or reserve[i] == j:
#                 physical.append(j)
#                 break
    
#     return len(set(physical))

# =========================
# 힌트를 참고한 풀이

def solution(n, lost, reserve):
    # 여벌옷을 가진 사람 중에 잃어버린 사람 제외(남에게 빌려줄 여벌옷을 갖고 있는 사람)
    reserve_real = set(reserve)-set(lost)
    # 잃어버린 사람 중에 여벌옷을 갖고 있는 사람 제외(남에게 여벌옷을 빌려야 하는 옷을 잃어버린 사람)
    lost_real = set(lost)-set(reserve)
    for i in reserve_real:
        if i-1 in lost_real:
            lost_real.remove(i-1)
        elif i+1 in lost_real:
            lost_real.remove(i+1)
    print(lost_real)
    return n-len(lost_real)



