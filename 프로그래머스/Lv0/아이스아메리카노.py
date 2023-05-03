def solution(money):
    num = money // 5500
    money2 = money % 5500
    return [num,money2]