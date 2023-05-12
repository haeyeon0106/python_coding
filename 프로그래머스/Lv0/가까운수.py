def solution(array, n):
    answer = 0
    array.sort()
    temp = []
    for i in array:
        temp.append(abs(i-n))
    
    return array[temp.index(min(temp))]