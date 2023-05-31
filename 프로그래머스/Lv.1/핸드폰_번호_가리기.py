def solution(phone_number):
    answer = ''
    for i in phone_number[:-4]:
        answer += "*"
    return answer+phone_number[-4:]

def solution2(phone_number):
    return "*"*(len(phone_number)-4) + phone_number[-4:]

print(solution2("01033334444"))