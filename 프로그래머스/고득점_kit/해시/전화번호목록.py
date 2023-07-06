def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
    return True\

# 다른 사람의 풀이
def solution2(phone_book):
    phone_book.sort()
    for p1,p2 in zip(phone_book,phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True

def solution3(phone_book):
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    
    for phone_number in phone_book:
        temp = ''
        for num in phone_number:
            temp += num

            # 현재 접두사가 해시맵에 있고 현재 번호와 접두사가 다른 경우
            if temp in hash_map and temp != phone_number:
                return False
    return True