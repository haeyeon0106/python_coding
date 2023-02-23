# #1
# class Calculator:
#     def __init__(self):
#         self.value = 0

#     def add(self,val):
#         self.value += val

# class UpgradeCaculator(Calculator):
#     def minus(self,val):
#         self.value -= val

# cal = UpgradeCaculator()
# cal.add(10)
# cal.minus(7)

# print(cal.value)

# #2
# class Calculator:
#     def __init__(self):
#         self.value = 0

#     def add(self,val):
#         self.value += val

# class MaxLimitCaculator(Calculator):
#     def add(self,val):
#         self.value += val
#         if self.value > 100:
#             self.value = 100

# cal = MaxLimitCaculator()
# cal.add(50)
# cal.add(60)

# print(cal.value)

# #3
# print(all([1,2,abs(-3)-3]))     #False
# print(chr(ord('a')) == 'a')     #True

# #4
# print(list(filter(lambda x:x>0,[1,-2,3,-5,8,-3])))

# #5
# print(int(0Xea))    # 234

# #6
# print(list(map(lambda x:x*3,[1,2,3,4])))

# #7
# a = [-8,2,7,5,-3,5,0,1]
# result = max(a) + min(a)
# print(result)

# #8
# div = 17 / 3
# print(round(div,4))

# #12
# import time
# print(time.strftime("%Y/%m/%d %H:%M:%S"))

# #13
import random

result = []

while len(result) < 6:
    num = random.randint(1,45)
    if num not in result:
        result.append(num)

print(result)



