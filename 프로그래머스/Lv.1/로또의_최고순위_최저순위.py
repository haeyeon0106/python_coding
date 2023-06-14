def rank(lotto_right):
    if lotto_right == 6:
        return 1
    elif lotto_right == 5:
        return 2
    elif lotto_right == 4:
        return 3
    elif lotto_right == 3:
        return 4
    elif lotto_right == 2:
        return 5
    else:
        return 6
def solution2(lottos, win_nums):
    answer = []
    result = 0
    zero = 0
    for lotto in lottos:
        if lotto in win_nums:
            result += 1
    zero = lottos.count(0)
    answer.append(rank(result+zero))
    answer.append(rank(result))
    return answer

def solution2(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]

def solution3(lottos, win_nums):
    rank = {
        0: 6,
        1: 6,
        2: 5,
        3: 4,
        4: 3,
        5: 2,
        6: 1
    }
    return [rank[len(set(lottos) & set(win_nums)) + lottos.count(0)], rank[len(set(lottos) & set(win_nums))]]

# 내 코드 간략화
def solution4(lottos, win_nums):
    result = 0
    rank = {0:6,1:6,2:5,3:4,4:3,5:2,6:1}
    for lotto in lottos:
        if lotto in win_nums:
            result += 1
    return rank[result+lottos.count(0)],rank[result]