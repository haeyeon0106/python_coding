def solution(num_list):
    last = num_list[-1]
    frontLast = num_list[-2]
    num_list.append(last - frontLast) if last > frontLast else num_list.append(last*2)
    return num_list

print(solution([2, 1, 6]))
print(solution([5, 2, 1, 7, 5]))