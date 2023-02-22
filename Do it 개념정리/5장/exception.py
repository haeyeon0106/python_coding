# try ~ except
# try : ... except [발생오류[as 오류 메세지 변수]]: ...

# ex
# try:
#     4/0
# except ZeroDivisionError as e:
#     print(e)

# IndexError가 발생할 때 오류 메세지 출력
# a = [1,2]
# try:
#     a[3]
# except IndexError as e:
#     print(e)

# try ~ finally 
# finally절은 try문 수행 도중 예외와 상관없이 항상 수행
# 사용한 리소스 close 해야할 때 많이 사용
# java -> try ~ catch문에서 default와 동일

# 두 개이상 오류 발견

# 인덱싱 오류가 먼저 발견되었으므로 ZeroDivisionError는 발생X
# try:
#     a = [1,2]
#     print(a[3])
#     4/0
# except IndexError as e:
#     print(e)
# except ZeroDivisionError as e:
#     print(e)

# try:
#     a = [1,2]
#     print(a[3])
#     4/0
# except (ZeroDivisionError,IndexError) as e:
#     print(e)

# 오류 피하기
# try:
#     f = open("나없는 파일",f)
# except FileExistsError:
#     pass

# 예외 만들기
class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)

try:
    say_nick('천사')
    say_nick('바보')
except MyError as e:
    print(e)

    
