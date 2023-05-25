def solution(chicken):
    answer = 0
    coupon = chicken
    while coupon >= 10:
        service = coupon // 10
        answer += service
        coupon = coupon%10 + service
    return answer

# 다른 사람 풀이
#프로그래머스 좋아요 많이 받은 순은 이해가 잘 안되고 
# 이해한다고 해도 내가 다른 문제에 적용을 못 시킬 거 같아 구글링하여 블로그를 참고한다
def solution2(chicken):
    answer = 0

    while chicken >= 10:
        # divmod 함수 이용하여 몫과 나머지를 구한다
        div,mod = divmod(chicken,10)
        # 서비스 받은 치킨 수
        answer += div
        # 남은 쿠폰의 개수
        chicken = div + mod
    return answer

print(solution2(100))