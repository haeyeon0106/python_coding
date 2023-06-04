def solution(price, money, count):
    answer = 0
    sum = 0     # 필요한 총 금액
    for i in range(1,count+1):
        sum += (price*i)    # 놀이기구 이용한 횟수만큼 필요한 이용료 더하기
    answer = (sum-money) if sum > money else 0
    return answer

# 다른 사람 풀이
def solution2(price,money,count):
    return max(0,price*(count+1)*count//2 - money)