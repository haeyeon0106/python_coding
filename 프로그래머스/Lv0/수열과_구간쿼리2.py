#정확성테스트에서 실패(수정필요)
def solution(arr, queries):
    answer = []
    li = []
    for s,e,k in queries:
        if k > max(arr[s:e+1]):
            answer.append(-1)
        else:
            li = [i for i in arr[s:e+1] if i > k]
            answer.append(min(li)) if li else answer.append(-1)
    return answer

print(solution([0, 1, 2, 4, 3],[[0, 4, 2],[0, 3, 2],[0, 2, 2]]))