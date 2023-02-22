# abs()
# 어떤 숫자를 입력하였을 때, 그 숫자의 절댓값을 돌려주는 함수
# n = abs(-5)
# print(n)

# all()
# 반복 가능한 자료형(ex.배열) x를 입력 인수로 받으며 x가 모두 참이면 T, 거짓이 하나라도 있으면 F
# bool = all([1,2,3])
# print(bool)
# bool = all([0,1,2,3])   # 0이 거짓이므로 False
# print(bool)

# any()
# 하나라도 참이면 T, 모두 거짓이면 F
# bool = all([0,""])
# print(bool)

# chr()
# 아스키 코드 값 입력받아 그 코드에 해당하는 문자 출력
# ch = chr(97)
# print(ch)

# ord(c)
# 문자의 아스키 코드 값을 돌려주는 함수
# print(ord('a'))

# dir()
# 객체가 자체적으로 가지고 있는 변수나 함수를 보여줌
# print(dir([1,2,3]))

# divmod(a,b)
# 2개의 숫자를 입력으로 받고 a를 b로 나눈 몫과 나머지를 튜플 형태로 돌려주는 함수
# print(divmod(45,6))

# enumerate
# 순서가 있는 자료형(리스트,튜플,문자열)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 돌려줌
# 객체가 현재 어느 위치에 있는지 알려 주는 인덱스 값이 필요할 때 유용
# for i, name in enumerate(['treasure','love','maker']):
#     print(i,name)

# eval
# 실행 가능한 문자열을 입력으로 받아 문자열을 실행한 결괏값을 돌려주는 함수
# 입력받은 문자열로 파이썬 함수나 클래스를 동적으로 실행하고 싶을 때 사용
# print(eval('10+21'))
# print(eval("'treasure'+'maker'"))   # 문자열을 연결하고 싶을 때 eval("[연결하고 싶은 문자열]")
# print(eval('divmod(4,3)'))


# filter(함수이름,반복가능한 자료형)
#  자료형이 함수에 입력되었을때 반환 값이 참인 것만 묶어서 반환
# def positive(x): return x>0
# print(list(filter(positive,[1,-3,2,0,-5,6])))   #람다: list(filter(lambda x:x>0,[1,-3,2,0,-5,6]))

# hex(c)
# 정수 값을 입력받아 16진수로 변환하여 돌려주는 함수
# print(hex(234))

# oct
# 정수 형태의 숫자를 8진수 문자열로 바꾸어 돌려주는 함수
# print(oct(34))

# id(object)
# 객체를 입력받아 객체의 고유 주소 값을 돌려주는 함수
# a = 3
# print(id(a))

# input()
# 사용자 입력 받는 함수
# name = input("이름>> ")
# print("내 이름은 {}입니다.".format(name))

# int(x)
# 문자열 형태의 숫자나 소수점이 있는 숫자 등을 정수 형태로 돌려주는 함수
# print(int('3'))
# num1 = int(input("정수1 입력>> "))
# num2 = int(input("정수2 입력>> "))
# print("두 정수의 합은 {}입니다.".format(num1+num2))

# isinstance(object,class)
# 입력으로 받은 인스턴스가 그 클래스의 인스턴스인지를 판단하여 참이면 T, 거짓이면 F
# class Person : pass
# a = Person()
# print(isinstance(a,Person))
# b = 3
# print(isinstance(b,Person))

# list(s)
# 반복 가능한 자료형 s를 입력받아 리스트로 만들어 돌려주는 함수
# print(list("python"))

# map(함수,반복 가능한 자료형)
# 입력받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려주는 함수
# print(list(map(lambda x:x*2,[1,2,3,4])))

# max,min
# 최대,최소 반환 함수(문자열도 가능)

# pow(x,y)
# x의 y 제곱한 결과값을 돌려주는 함수
# print(pow(2,4))

# range
# for문과 자주 사용 / 입력받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 생성
# print(list(range(5)))     # 숫자를 지정하지 않으면 0부터 시작
# print(list(range(5,10)))  # 인수 2개 => 시작숫자와 끝 숫자(범위에 포함x)
# print(list(range(1,10,2)))  # 인수 3개 => 시작 숫자, 끝 숫자, 숫자 간 사이

# round()
# 숫자 반올림
# print(round(5.3))
# print(round(4.365,1))   #4.4

# sorted
# 입력값을 정렬한 후 그 결과를 리스트로 돌려줌
# print(sorted([5,8,1]))
# print(sorted('orange'))

# str(object)
# 문자열 형태로 객체를 변환하여 돌려주는 함수
# print(str(3)+str(5))    #35
# print(str('hi'.upper()))    #HI

# type(object)
# 입력값의 자료형이 무엇인지 알려 주는 함수
# print(type(3))  #<class 'int'>

# zip(반복가능한 자료형)
# 동일한 개수로 이루어진 자료형을 묶어주는 역할
# print(list(zip([1,2,3],[4,5,6])))   # [(1, 4), (2, 5), (3, 6)]