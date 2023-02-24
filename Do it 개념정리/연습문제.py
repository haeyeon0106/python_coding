# #1
# str = "a:b:c:d"
# list = str.split(":")
# result = "#".join(list)
# print(result)

# #2
# a = {'A':90, 'B':80}
# print(a.get('C',70))

# #4
# A = [20,55,67,82,45,33,90,87,100,25]
# great = list(filter(lambda x:x>=50,A))
# sum = 0
# for i in great:
#     sum += i
# print(sum)

# #5
# def fin(n):
#     if n == 0 : return 0
#     if n == 1 : return 1
#     return fin(n-1)+fin(n-2)

# for i in range(10):
#     print(fin(i))

# #6
# user_input = input("숫자를 입력하시오>> ")
# number = user_input.split(",")

# result = 0
# for i in number:
#     result += int(i)
# print(result)

# #7
# number = int(input("구구단을 출력할 숫자를 입력하세요(2~9): "))

# for i in range(1,10):
#     print(number*i , end= " ")

# #8
# f = open('abc.txt','r')
# lines = f.readlines()
# f.close()

# #9

# #10
# class Calculator:
#     def __init__(self,numberList):
#         self.numberList = numberList

#     def sum(self):
#         result = 0
#         for i in self.numberList:
#             result += i
#         return result
    
#     def avg(self):
#         return self.sum() / len(self.numberList)
    
# cal1 = Calculator([1,2,3,4,5])
# print(cal1.sum())
# print(cal1.avg())

# cal2 = Calculator([6,7,8,9,10])
# print(cal2.sum())
# print(cal2.avg())

# #13
# data = "4546793"

# number = list(map(int,data))
# result = []

# for i, nums in enumerate(number):
#     result.append(str(nums))

#     if i < len(number)-1:
#         odd = nums % 2 == 1
#         next_odd = number[i+1] % 2 == 1

#         if odd and next_odd:
#             result.append("-")
#         elif not (odd or next_odd):
#             result.append('*')

# print("".join(result))

# #14       // 이해 안 감
# data = "aaabbcccccca"

# count = list(map(str,data))

# for i,nums in enumerate(count):


# #15   // 재도전 필요
# def check(s):
#     result = []
#     for i in s:
#         if i not in result:
#             result.append(i)
#         else: return False
#     return len(result) == 10
    
# print(check("0123456789"))
# print(check("01234"))
# print(check("01234567890"))
# print(check("6789012345"))
# print(check("0123456323789"))

# #16 - 17 문풀 완료

# #19
# import re

# data = """
#     Lee 010-1997-0330
#     So 010-2005-0218
#     Kim 010-1997-0808
# """
# phone = re.compile("(\d{3}[-]\d{4})[-]\d{4}")
# print(phone.sub("\g<1>--####",data))

# #20  // 다시 풀기
