def solution(my_string):
    return eval(my_string)
    

# 좋아요 많이 받은 풀이

# 연산자 -를 +로 대체하고 뒤에 있는 수를 음수로 만들어서 계산
def solution2(my_string):
    return sum(int(i) for i in my_string.replace("-","+ -").split('+'))

print(solution2("3 + 4"))

