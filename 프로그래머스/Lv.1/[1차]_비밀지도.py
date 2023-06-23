def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        a = bin(arr1[i]|arr2[i])[2:].zfill(n)
        b = a.replace('1','#').replace('0',' ')
        answer.append(b)
    return answer

def solution2(n, arr1, arr2):
    answer = []
    for i in range(n):
        a = bin(arr1[i]|arr2[i])[2:].zfill(n)
        c = a.maketrans({'1':'#','0':' '})
        answer.append(a.translate(c))
    return answer