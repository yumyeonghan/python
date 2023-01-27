# 괄호 변환(dfs)

def devide(p):
    count_l = 0
    count_r = 0
    for i in range(len(p)):
        if p[i] == "(":
            count_l += 1
        else:
            count_r += 1
        if count_l == count_r:
            return p[:i + 1], p[i + 1:]

def check(u):
    count = 0
    for i in range(len(u)):
        if u[i] == "(":
            count += 1
        else:
            count -= 1
        if count < 0:
            return False
    
    if count != 0:
        return False
    return True
        
def solution(p):
    answer = ""
    
    if p == "":
        return ""
    
    u, v = devide(p)
    
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