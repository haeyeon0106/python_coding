import collections
# 정확성은 통과했지만 효율성은 통과하지 못함
def solution(participant, completion):
    answer = ''
    for i in participant:
        if i not in completion:
            answer += i
        elif participant.count(i) != completion.count(i):
            answer += i
            participant.remove(i)
    return answer

def solution2(participant, completion):
    answer = ''
    hash = {}
    for name in participant:
        if name in hash:
            hash[name] += 1
        else:
            hash[name] = 1
    for com in completion:
        hash[com] -= 1
    for name,num in hash.items():
        if num > 0:
            answer += name
    return answer

def solution3(participant,completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    print(collections.Counter(participant))
    return list(answer.keys())[0]

def solution4(participant,completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]

print(solution4(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))