# 1000미만의 자연수에서 3과 5의 배수 총합 구하기

# sum = 0 
# for n in range(1,1000):
#     if n % 3 == 0 or n % 5 == 0:
#         sum += n
# print(sum)

# 게시판 페이징하기
# 총 게시물 건 수(m)     페이지당 보여줄 게시물 수(n)   페이지 수
#       5                       10                      1
#       15                      10                      2
#       25                      10                      3
#       30                      10                      3

# (총 페이지 수) = (총 게시물 건수) / (페이지당 보여줄 게시물 수) + 1

# def getTotalPage(m,n):
#     if m % n == 0:
#         return m // n
#     else:
#         return m //n + 1

# print(getTotalPage(5,10))
# print(getTotalPage(15,10))
# print(getTotalPage(25,10))
# print(getTotalPage(30,10))

# 간단한 메모장 만들기
# memo.py => 입출력은 문제 풀면서 익히기로 함

