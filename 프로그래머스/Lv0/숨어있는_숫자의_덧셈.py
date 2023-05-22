# my_string에서 문자인지 판별한 후 문자라면 공백으로 변환
# 숫자가 아닌 자리를 공백으로 변환한 문자열을 공백으로 자름
# 공백으로 자른 문자열의 원소를 int 변환하고 list에 담은 후 sum으로 반환

def solution(my_string):
    answer = 0
    for i in my_string:
        if i.isalpha():
            my_string = my_string.replace(i," ")
    my_string = my_string.split()
    return sum(list(map(int,my_string)))

# 다른 사람 풀이
def solution2(my_string):
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    return sum(int(i) for i in s.split())


