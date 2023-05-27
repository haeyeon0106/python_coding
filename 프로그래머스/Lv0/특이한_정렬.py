def solution(numlist, n):
    # lambda를 이용한 리스트 정렬
    # abs(x-n)로 정렬 후 값이 같다면 n-x로 정렬
    result = sorted(numlist,key=lambda x:(abs(x-n),n-x))
    return result

# 다른 풀이
def solution2(numlist, n):
    # abs(x-n)가 동일하면 원소 중 내림차순으로 정렬
    # ex) abs(5-4) == abs(3-4)이므로 -x로 정렬할 시 5,3 순으로 정렬
    result = sorted(numlist,key=lambda x:(abs(x-n),-x))
    return result

def solution3(numlist, n):
    # num -> (abs(n-num), -num)
    numlist = [(abs(n-num), -num) for num in numlist]
    # [(3, -1), (2, -2), (1, -3), (0, -4), (1, -5), (2, -6)]

    # 첫 번째 요소를 기준으로 오름차순 정렬 and 두 번째 요소를 기준으로 내림차순 정렬
    numlist.sort()
    # [(0, -4), (1, -5), (1, -3), (2, -6), (2, -2), (3, -1)]

    # 두 번쨰 요소만 반환
    return [-num for _, num in numlist]

def solution4(numlist,n):
    return [-x[1] for x in sorted([(abs(k-n),-k)for k in numlist])]

print(solution3([1, 2, 3, 4, 5, 6],4))