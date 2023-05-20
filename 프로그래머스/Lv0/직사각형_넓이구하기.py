def solution(dots):
    answer = 0
    x_li = []
    y_li = []
    for i in dots:
        x = i[0]
        y = i[1]
        x_li.append(x)
        y_li.append(y)
    x_li = list(set(x_li))
    y_li = list(set(y_li))
    answer = (max(x_li)-min(x_li))*(max(y_li)-min(y_li))
    return answer