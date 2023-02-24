# 정규표현식
# 복잡한 문자열을 처리할 때 사용하는 기법

# Q. 주민등록번호를 포함하고 있는 텍스트가 있다. 이 텍스트에 포함된 모든 주민등록번호의 뒷자리를 * 문자로 변경

# # 정규표현식 적용 전
# data = """"
# jung 050218-4132874
# jae 010823-4298475
# """

# result = []
# for line in data.split("\n"):
#     word_result=[]
#     for word in line.split(" "):
#         if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():   # 전체 문자 길이 14 & (-)앞자리 숫자 & (-) 뒷자리 숫자
#             word = word[:7]+"-"+"*******"
#         word_result.append(word)
#     result.append(" ".join(word_result))

# print("\n".join(result))

# 정규표현식 적용 후
import re   # 정규 표현식을 사용하기 위한 모듈

data = """
jung 050218-4132874
jae 010823-4298475
"""

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******",data))