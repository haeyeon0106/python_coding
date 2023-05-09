def solution(s):
    answer = 0
    num_word = ["zero","one","two","three","four","five",
                "six","seven","eight","nine"]
    
    for i,j in enumerate(num_word):
        s = str(i).join(s.split(j))
        
    return int(s)


def solution2(s):
    num_word = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    
    for i,j in num_word.items():
        s = s.replace(i,j)
        
    return int(s)

print(solution("one4seveneight"))