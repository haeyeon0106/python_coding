def solution(survey, choices):
    answer = ''
    type = {'R':0,'T':0,'C':0,'F':0,'J':0,
           'M':0,'A':0,'N':0}
    agree = {1:3,2:2,3:1,4:0,5:1,6:2,7:3}
    
    for i in range(len(choices)):
        if 1 <= choices[i] <= 3:
            type[survey[i][0]] += agree[choices[i]]
        elif 5 <= choices[i] <= 7:
            type[survey[i][1]] += agree[choices[i]]
    
    answer += 'R' if type['R'] >= type['T'] else 'T'
    answer += 'C' if type['C'] >= type['F'] else 'F'
    answer += 'J' if type['J'] >= type['M'] else 'M'
    answer += 'A' if type['A'] >= type['N'] else 'N'
    return answer
