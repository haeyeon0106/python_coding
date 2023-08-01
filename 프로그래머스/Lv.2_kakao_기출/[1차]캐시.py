def solution(cacheSize, cities):
    answer = 0
    cache = []
    cities = list(map(str.lower,cities))    
    for city in cities:
        if city not in cache:
            if cacheSize == 0:
                answer += 5
                continue
            elif len(cache) < cacheSize:
                cache.append(city)
            elif len(cache) >= cacheSize:
                cache.pop(0)
                cache.append(city)
            answer += 5    
        else:
            cache.pop(cache.index(city))
            cache.append(city)
            answer += 1
    return answer

# 위 코드 간략화 및 설명 추가
def solution2(cacheSize, cities):
    answer = 0
    cache = []
    
    # 리스트의 모든 원소 소문자로 변환(대소문자 구분X)
    cities = list(map(str.lower,cities))
    
    if cacheSize == 0:
        return len(cities)*5
    
    for city in cities:
        if city not in cache:
            
            # cities 원소가 들어갈 cache의 크기가 cacheSize보다 작다면 삽입
            if len(cache) < cacheSize:
                cache.append(city)
            # 크다면 맨 앞의 원소 제거 후 마지막에 삽입
            else:
                cache.pop(0)
                cache.append(city)
            answer += 5
        
        # city가 cache에 있을 경우
        else:
            # city를 cache 리스트에서 제거
            cache.pop(cache.index(city))
            # 맨 뒤로 삽입
            cache.append(city)
            answer += 1
    return answer

# ==== 다른 사람 풀이 ====
def solution3(cacheSize,cities):
    import collections
    cache = collections.deque(maxlen=cacheSize)
    time = 0

    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time
