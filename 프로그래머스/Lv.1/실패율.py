def solution(N,stages):
    answer = []
    fail = {}       # 실패율
    all_player = len(stages)    # 총 플레이어수
    for i in range(1,N+1):
        if all_player == 0 :    # 스테이지에 도달한 플레이어 수가 0일 경우
            fail[i] = 0
        else:
            fail[i] = stages.count(i) / all_player
            all_player -= stages.count(i)
    answer = sorted(fail,key=lambda x:fail[x],reverse=True) # 스테이지 실패율을 기준으로 내림차순으로 정렬
    return answer


