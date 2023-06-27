def solution(id_list, report, k):
    answer = [0]*len(id_list)
    warn = {}
    warn_count = {}
    
    for re in list(set(report)):
        repo = re.split()
        if repo[0] not in warn:
            warn[repo[0]] = []
        warn[repo[0]].append(repo[1])
        
        # 신고횟수 구하기
        if repo[1] not in warn_count:
            warn_count[repo[1]] = 1
        else:
            warn_count[repo[1]] += 1
    
    # 경고 횟수 넘어간 사용자
    limit = [key for key, value in warn_count.items() if value >= k]
    
    for idx,id in enumerate(id_list):
        if id in warn:
            for lim in limit: 
                if lim in warn[id]: 
                    answer[idx] += 1        
    return answer