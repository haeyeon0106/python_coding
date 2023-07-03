import functools
def solution(numbers):
    numbers = list(map(str,numbers))
    numbers.sort(key=lambda x:x*3,reverse=True)
    # lambda x:x*3은 6 -> 666 / 2 -> 222 / 10 -> 101010
    # 문자열 비교는 맨 앞부터 비교하므로 [10,2,6]인데 reverse=True(내림차순)하면 [6,2,10]이다. 
    answer = ''.join(numbers)
    return str(int(answer))

# ========= 다른 사람 풀이 =======
def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1)>int(t2)) - (int(t1)<int(t2))

def solution2(numbers):
    n = list(map(str,numbers))
    n = sorted(n,key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer

