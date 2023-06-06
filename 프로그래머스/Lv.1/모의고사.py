# 결국 통과하지 못한 나의 길고 긴 코드...ㅠ
def list_compare(answers,shoot):
    a = len(answers)
    s = len(shoot)
    if a > s:
        if a % s == 0:
            shoot = shoot*(a//s)
        else:
            shoot += shoot[:a%s]
    else:
        shoot = shoot[:len(answers)]
    return shoot

def answer_compare(answers,shoot):
    count = 0
    for a,s in zip(answers,shoot):
        if a == s:
            count += 1
    return count

def solution(answers):
    answer = []
    no1 = [1,2,3,4,5]
    no2 = [2,1,2,3,2,4,2,5]
    no3 = [3,3,1,1,2,2,4,4,5,5]
    n1 = list_compare(answers,no1)
    n2 = list_compare(answers,no2)
    n3 = list_compare(answers,no3)
    x1 = answer_compare(answers,n1)
    x2 = answer_compare(answers,n2)
    x3 = answer_compare(answers,n3)
    shoot = [x1,x2,x3]
    answer = [i+1 for i,x in enumerate(shoot) if x == max(shoot)]
    return answer

# 다른 사람의 풀이를 참고한 코드
def solution2(answers):
    result = []
    shoots = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    scores = [0,0,0]

    for i,answer in enumerate(answers):
        for j,shoot in enumerate(shoots):
            if answer == shoot[i%len(shoot)]:
                scores[j] += 1
    return [i+1 for i,score in enumerate(scores) if score == max(scores)]

print(solution2([1,2,3,4,5]))
print(solution2([1,3,2,4,2]))