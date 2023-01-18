# 외벽 점검
# 외벽 점검
from itertools import permutations

def solution(n, weak, dist):
    
    lenth = len(weak)
    
    for i in range(len(weak)):
        weak.append(weak[i] + n)
    
    answer = len(dist) + 1
    
    for start in range(lenth):
        
        for person in list(permutations(dist, len(dist))):
            count = 1
            position = weak[start] + person[count - 1]
            
            for index in range(start, start + lenth):
                if position < weak[index]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[index] + person[count - 1]
            answer = min(answer, count)
    
    if answer > len(dist):
        return -1
    
    return answer