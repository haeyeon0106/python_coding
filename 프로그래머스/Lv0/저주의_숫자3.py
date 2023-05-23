
# i가 1부터 answer에 1을 더한다 (i는 10진법, answer는 3x 마을에서 사용하는 수)
# answer가 3의 배수이거나 3이 포함될 때까지(while) answer에 1을 더한다
def solution(n):
    answer = 0
    for i in range(1,n+1):
        answer+=1
        while answer % 3 == 0 or '3' in str(answer):
            answer+=1
    return answer

# 다른 사람 풀이

# 3의 배수와 3이 포함된 수를 판별하는 함수 생성
# not을 붙여 위의 조건에 해당되면 False 반환하고 filter 함수를 사용해 False로 반환된 수를 제외한 수를 listf로 담고
# 0 인덱스부터 시작하므로 입력되는 수에 -1을 하여 답 추출
def is_use_three(number):
    if "3" in str(number):
        return True
    if number % 3 == 0:
        return True
    return False


def solution2(n):  
    return list(filter(lambda v: not is_use_three(v), range(200)))[n-1]

print(solution2(15))