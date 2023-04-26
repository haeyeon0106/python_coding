# def solution(my_string, overwrite_string, s):
#     answer = ''
#     answer += my_string[0:s]
#     answer += overwrite_string
#     n = len(my_string) - len(answer)
#     if(len(my_string) > len(answer)):
#         answer += my_string[-n:]

#     return answer

def solution(my_string, overwrite_string, s):
    answer = my_string[0:s]+overwrite_string+my_string[s+len(overwrite_string):]
    return answer

print(solution("He11oWor1d","lloWorl",2))
print(solution("Program29b8UYP","merS123",7))