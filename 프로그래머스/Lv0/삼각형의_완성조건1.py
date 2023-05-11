def solution(sides):
    a = max(sides)
    sides.remove(a)
    result = sum(sides)
    return 1 if a < result else 2