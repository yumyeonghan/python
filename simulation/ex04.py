# 문자열 압축
def solution(s):
    answer = len(s)
    
    for step in range(1, len(s) // 2 + 1):
        비교 = ""
        count = 1
        prev = s[:step]
        
        for j in range(step, len(s), step):
            if s[j:j + step] == prev:
                count += 1
            else:
                비교 += str(count) + prev if count > 1 else prev
                prev = s[j: j + step]
                count = 1
        
        비교 += str(count) + prev if count > 1 else prev
        answer = min(answer, len(비교))
        
    return answer