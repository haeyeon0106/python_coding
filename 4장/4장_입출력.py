# 파일 읽고 쓰기

# writeline.py
# f = open("C:/Users/lg/OneDrive/바탕 화면/coding_test/새파일.txt",'w')
# for i in range(1,11):
#     data = "%d번째 줄입니다.\n" %i
#     f.write(data)
# f.close()

# # readline.py
# f = open("C:/Users/lg/OneDrive/바탕 화면/coding_test/새파일.txt",'r')
# line = f.readline()
# print(line)
# f.close()

# readline_all.py
# f = open("C:/Users/lg/OneDrive/바탕 화면/coding_test/새파일.txt",'r')
# while True:
#     line = f.readline()
#     if not line: break
#     print(line)
# f.close()

# readlines함수.py
# f = open("C:/Users/lg/OneDrive/바탕 화면/coding_test/새파일.txt",'r')
# line = f.readlines()
# print(line)
# f.close()

# read함수.py
# f = open("C:/Users/lg/OneDrive/바탕 화면/coding_test/새파일.txt",'r')
# line = f.read()
# print(line)
# f.close()

# with함수로 객체f가 자동으로 close
# with open("C:/Users/lg/OneDrive/바탕 화면/coding_test/새파일.txt",'w') as f:
#     f.write("Life is too short, you need python")

# ==============연습문제==============

# #1
# def is_odd(number):
#     if number % 2 == 1:
#         return True
#     else:
#         return False

# print(is_odd(15))

# #2
# def avg_numbers(*arg):
#     result = 0
#     for i in arg:
#         result += i
#     return result / (len(arg))

# print(avg_numbers(1,2))
# print(avg_numbers(1,2,3,4,5))


# #3
# input1 = int(input("첫번째 숫자 입력>> "))
# input2 = int(input("첫번째 숫자 입력>> "))

# total = input1 + input2
# print("두 수의 합은 %d입니다." %total)

# #5
# f1 = open("test.txt",'w')
# f1.write("Life is too short")
# f1.close()

# f2 = open("test.txt","r")
# print(f2.read())

# #6
# user_input = input("저장할 내용을 입력하세요:")
# f = open("test.txt",'a')
# f.write(user_input)
# f.write("\n")
# f.close()

# #7
f = open("test2.txt",'r')
body = f.read()
f.close()

body = body.replace("java","python")

f = open("test2.txt","w")
f.write(body)
f.close()