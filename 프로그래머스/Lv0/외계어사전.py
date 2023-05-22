def solution(spell, dic):
    spell = "".join(sorted(spell))
    print(spell)
    for i in dic:
        i = "".join(sorted(i))
        if spell == i:
            return 1
        # 굳이 join해서 문자로 안만들고 sorted로 해결해도 됨
        # if sorted(spell) == sorted(i):
        #     return 1
    return 2

# 다른 사람 풀이
def solution2(spell,dic):
    spell = set(spell)
    for i in dic:
        if not spell-set(i):
            return 1
    return 2

print(solution2(["p", "o", "s"],["sod", "eocd", "qixm", "adio", "soo"]))
