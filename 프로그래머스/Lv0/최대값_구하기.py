def solution(numbers):
    # answer = 0
    # li = list(sorted(numbers))
    # answer = li[-2]*li[-1]
    numbers.sort()
    return numbers[-2]*numbers[-1]