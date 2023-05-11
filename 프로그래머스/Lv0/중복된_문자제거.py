def solution(my_string):
    answer = ''
    word = []
    for i in my_string:
        if i not in word:
            word.append(i)
    answer = "".join(word)
    return answer