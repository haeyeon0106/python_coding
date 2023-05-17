def solution(array):
    answer = 0
    for i in array:
        for j in str(i):
            answer += j.count("7")
    return answer

# 다른 사람 풀이
def solution2(array):
    return str(array).count("7")

def solution3(array):
    # "".join(map(str,array)) => 리스트의 숫자를 문자형으로 변환 후 하나로 연결 (77717)
    return "".join(map(str,array)).count('7')

print(solution2([7, 77, 17]))