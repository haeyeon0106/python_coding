# 평행 조건
# 두 직선의 기울기가 같아야 한다
# 모든 경우의 수를 구현한다
# 평행 조건은 알았지만 구현 방법이 감이 안잡혔다.
# 테스트케이스 2번 오류 -> 기울기가 소수점일 때도 생각한다

def slope(a,b):
    return (a[1] - b[1]) / (a[0] - b[0])
def solution(dots):
    answer = 0
    if slope(dots[0],dots[1]) == slope(dots[2],dots[3]):
        answer = 1
    elif slope(dots[0],dots[2]) == slope(dots[1],dots[3]):
        answer = 1
    elif slope(dots[0],dots[3]) == slope(dots[2],dots[1]):
        answer = 1
    return answer