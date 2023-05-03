#정확성테스트에서 실패(수정필요)
def solution(arr, queries):
    answer = []
    nums = []
    for s,e,k in queries:
        for i in range(s,e+1):
            a = arr[i]
            if a > k:
                if a > arr[i]:
                    a = arr[i]
            else: a = -1
        answer.append(a)
        
    return answer

print(solution([0, 1, 2, 4, 3],[[0, 4, 2],[0, 3, 2],[0, 2, 2]]))