from itertools import combinations
def solution(number):
    answer = 0
    answer = list(map(sum,list(combinations(number,3)))).count(0)
    return answer

def solution2(number):
    answer = 0
    for i in range(0,len(number)-2):
        for j in range(i+1,len(number)-1):
            for z in range(j+1,len(number)):
                if number[i] + number[j] + number[z] == 0:
                    answer += 1
    return answer

print(solution2([-3, -2, -1, 0, 1, 2, 3]))