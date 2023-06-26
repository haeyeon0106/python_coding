def find_index(num):
    key_pad = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    row,col = 0,0
    for i in range(len(key_pad)):
        if num in key_pad[i]:
            row = i
            col = key_pad[i].index(num)
    return [row,col]

def solution(numbers, hand):
    answer = ''
    left,right = [1,4,7],[3,6,9]
    left_index = [3,0]
    right_index = [3,2]
    for num in numbers:
        if num in left:
            answer+='L'
            left_index = find_index(num)
        elif num in right:
            answer += 'R'
            right_index = find_index(num)
        else:
            middle = find_index(num)
            L = abs(middle[0]-left_index[0])+abs(middle[1]-left_index[1])
            R = abs(middle[0]-right_index[0])+abs(middle[1]-right_index[1])
            if L > R:
                answer += 'R'
                right_index = middle
            elif L < R:
                answer += 'L'
                left_index = middle
            else:
                if hand == 'right':
                    answer += 'R'
                    right_index = middle
                else:
                    answer += 'L'
                    left_index = middle
    return answer