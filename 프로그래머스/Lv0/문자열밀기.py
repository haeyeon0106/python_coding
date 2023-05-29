# deque를 이용
# 그래도 과거의 기억으로 rotate로 풀어야 한다고 감이 왔다
# 여러 방법으로 지지고 볶고 하다가 결국 도움을 받아 통과하였다.
from collections import deque
def solution(A, B):
    answer = 0
    A,B = deque(A),deque(B)
    for i in range(len(A)):
        if A == B:
            return i
        A.rotate(1)
    return -1

# 문자열 슬라이싱
def solution2(A,B):
    for i in range(len(A)):
        if A == B:
            return i
        A = A[-1]+A[:-1]
    return -1

# insert, pop 이용
def solution3(A,B):
    for i in range(len(A)):
        if A == B:
            return i
        A.insert(0,A.pop())
    return -1

# find
# B가 ohell라면 BB는 ohellohell이다
# A가 hello이고 BB.find(A)면 hello가 사작되는 인덱스 1을 반환
# 만약 없다면 find 함수의 특징인 -1을 반환
def solution4(A,B):
    BB = B*2
    return BB.find(A)