def solution(cipher, code):
    answer = ''
    i = 1
    while code*i <= len(cipher):
        answer += cipher[code*i-1]
        i += 1
    return answer