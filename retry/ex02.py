# 문자열 압축
def solution(s):
    answer = len(s)
   
    for step in range(1, len(s)//2 + 1):
        value = s[:step]
        count = 1
        tmp = ""
        
        for j in range(step, len(s), step):
            if value == s[j: j + step]:
                count += 1
            else:
                tmp += str(count) + value if count > 1 else value
                value = s[j: j + step]
                count = 1
        tmp += str(count) + value if count > 1 else value
        answer = min(answer, len(tmp))    
    
    return answer