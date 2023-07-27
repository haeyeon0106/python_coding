# === 테스트 케이스 5,11 통과X / 효율성은 완료 ===
def solution(s):
    if s[0] == ')' or s[-1] == '(' or s.count(')') != s.count('('):
        return False
    return True

# === 테스트 케이스 모두 통과하였지만 효율성 1번에서 오류 ===
# 이유 count() 함수는 모든 요소를 순회하기 때문에 시간복잡도가 O(n^2)가 된다.
def solution2(s):
    stack = []
    if s[0] == ')' or s[-1] == '(' or s.count(')') != s.count('('):
        return False
    for i in s:
        if i == ')' and stack.count(')') >= stack.count('('):
            return False
        stack.append(i)
    return True

# === 내가 푼 코드 ===
def solution3(s):
    stack = []

    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    
    return len(stack) == 0

# === 다른 사람이 푼 코드 ===
def solution4(s):
    stack = []

    for i in s:
        if len(stack) == 0 and i == ')':
            return False
        if i == ')' and stack[-1] == '(':
            stack.pop()
        if i == '(':
            stack.append(i)
    
    return len(stack) == 0