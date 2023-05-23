# ex) [[0, 1], [2, 5], [3, 9]]
# sets = [{0},{2,3,4},{3,4,5,6,7,8}]
# sets[0]&sets[1] = {}
# sets[0]&sets[2] = {}
# sets[1]&sets[2] = {3,4}
# len(sets[0]&sets[1] | sets[0]&sets[2] | sets[1]&sets[2]) = 2
def solution(lines):
    sets = [set(range(min(l),max(l))) for l in lines]
    return len(sets[0]&sets[1] | sets[0]&sets[2] | sets[1]&sets[2])

# 다른 사람 풀이
