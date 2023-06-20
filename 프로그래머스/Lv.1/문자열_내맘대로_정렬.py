# 나의 풀이
def solution(strings, n):
    return sorted(strings,key=lambda x:(x[n],x))

# 다른 사람 풀이
def solution2(strings,n):
    new = []
    answer = []
    for i in strings:
        a = i[n]    # 주어진 인덱스의 알파벳을 앞에 넣어준다.
        b = a+i
        new.append(b)
    new.sort()
    for i in new:
        answer.append(i[1:])    # 정렬 후 추가한 알파벳을 제외한 나머지 단어만 리스트에 삽입
    return answer

# 위의 코드 좀 더 단순히
def solution3(strings,n):
    for i,x in enumerate(strings):
        strings[i] = x[n] + x
    return [i[1:] for i in sorted(strings)]

print(solution3(["sun", "bed", "car"],1))
print(solution3(["abce", "abcd", "cdx"],2))

