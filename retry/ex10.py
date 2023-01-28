# 괄호 변환(dfs)

def divide(p):
    count = 0
    for i in range(len(p)):
        if p[i] == "(":
            count += 1
        else:
            count -= 1
        
        if count == 0:
            return p[:i + 1], p[i + 1:]

def check(u):
    stack = []
    for i in range(len(u)):
        if u[i] == "(":
            stack.append("(")
        else:
            if stack:
                stack.pop()
            else:
                return False
    
    if stack:
        return False
    return True

def solution(p):
    answer = ""
    if p == "":
        return ""
    
    u, v = divide(p)
    if check(u):
        return u + solution(v)
    else:
        answer += "("
        answer += solution(v)
        answer += ")"
        
        for i in u[1:-1]:
            if i == "(":
                answer += ")"
            else:
                answer += "("
        return answer
    
    return answer