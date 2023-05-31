def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if int(signs[i]) == 1:
            answer += absolutes[i]
        else:
            answer += absolutes[i]*(-1)
    return answer

def solution2(absolutes,signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))

print(solution2([4,7,12],["true","false","true"]))