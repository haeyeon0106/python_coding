def solution(record):
    answer = []
    uid_nick = {}
    uid_state = []
    for r in record:
        r = r.split(' ')
        if r[0] == 'Enter':
            uid_nick[r[1]] = r[2]
            r = [r[0],r[1]]
            uid_state.append(r)
        elif r[0] == 'Change':
            uid_nick[r[1]] = r[2] 
        elif r[0] == 'Leave':
            uid_state.append(r)
    
    for state,uid in uid_state:
        if state == 'Enter':
            msg = uid_nick[uid] + '님이 들어왔습니다.'
            answer.append(msg)
        elif state == 'Leave':
            msg = uid_nick[uid] + '님이 나갔습니다.'
            answer.append(msg)
    return answer

# === 다른 사람 풀이 ===
def solution(record):
    userDict = {}
    answer = []
    
    for line in record:
        line = line.split(' ')
        if line[0] == 'Enter':
            userDict[line[1]] = line[2]
        elif line[0] == 'Change':
            userDict[line[1]] = line[2]
    
    for line in record:
        line = line.split(' ')
        msg = userDict[line[1]]
        if line[0] == 'Enter':
            msg += '님이 들어왔습니다.'
        elif line[0] == 'Leave':
            msg += '님이 나갔습니다.'
        else:
            continue
        answer.append(msg)
    return answer