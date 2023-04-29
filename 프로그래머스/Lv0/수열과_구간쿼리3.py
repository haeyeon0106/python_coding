def solution(arr, queries):
    for i in range(len(queries)):
        a = queries[i][0]
        b = queries[i][1]
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp
    return arr