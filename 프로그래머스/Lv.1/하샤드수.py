def solution(x):
    count = 0
    for i in str(x):
        count += int(i)
    if x % count == 0:
        return True
    return False