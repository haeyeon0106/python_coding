def solution(x1, x2, x3, x4):
    answer = True
    bool1 = False if x1 == False and x2 == False else True
    bool2 = False if x3 == False and x4 == False else True
    answer = True if bool1 == True and bool2 == True else False

    # answer = (x1|x2) & (x3|x4)
    return answer