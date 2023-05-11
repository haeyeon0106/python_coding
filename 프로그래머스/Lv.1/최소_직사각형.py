def solution(sizes):
    answer = 0
    temp = 0
    max_w = 0
    max_h = 0
    for w,h in sizes:
        if w < h : 
            temp = w
            w = h
            h = temp
        if max_w < w:
            max_w = w
        if max_h < h:
            max_h = h
    return max_w * max_h

# 다른 사람 풀이
def solution2(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)

print(solution2([[60, 50], [30, 70], [60, 30], [80, 40]]))