def solution(s):
    answer = []
    # 문자열 s에서 숫자만 분할
    s_chan = s[2:-2].split('},{')
    result = []

    # 리스트의 각 요소를 ','로 분할
    for i in s_chan:
        result.append(i.split(','))
    
    # [[2],[2,1],[2,1,4,3],[2,1,3]](예시)를 각 요소의 길이순으로 정렬
    result = sorted(result,key=len)

    # 요소가 answer에 없다면 정수로 바꿔 대입
    for i in range(len(result)):
        for j in result[i]:
            if int(j) not in answer:
                answer.append(int(j))
    return answer

# === 다른 사람 풀이 ===
def solution2(s):
    answer = []
    s1 = s.lstrip('{').rstrip('}').split('},{')
    new_s = []
    for i in s1:
        new_s.append(i.split(','))
    new_s.sort(key=len)
    
    for i in range(len(new_s)):
        for j in new_s[i]:
            if int(j) not in answer:
                answer.append(int(j))
    return answer

def solution3(s):
    # {{, }}를 제거 후 },{ 으로 나누기
    data = s[2:-2].split("},{")
    # 길이 별로 오름차순 정렬
    data = sorted(data, key=lambda x: len(x))
    answer = []
    for item in data:
        # 각각의 원소로 분류 후
        item = list(map(int, item.split(",")))
        for value in item:
            # 포함되어 있지 않으면 input
            if value not in answer:
                answer.append(value)
    return answer