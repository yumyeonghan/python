# 기둥과 보 설치
def check(answer):
    for x, y, a in answer:
        if a == 0:
            if y == 0 or [x, y, 1] in answer or [x - 1, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            else:
                return False
        
        if a == 1:
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            else:
                return False
        
        return True                            
                
def solution(n, build_frame):
    answer = []
    
    for x, y, a, b in build_frame:
        if b == 1:
            answer.append([x, y, a])
            if check(answer) == False:
                answer.remove([x, y, a])
                
        else:
            answer.remove([x, y, a])
            if check(answer) == False:
                answer.append([x, y, a])
    
    return sorted(answer)
