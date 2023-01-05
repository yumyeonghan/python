# 자물쇠와 열쇠
import copy

def turn_left(key):
    new_key = [[0]*len(key) for _ in range(len(key))]
    
    for i in range(len(key)):
        for j in range(len(key)):
            new_key[j][len(key) - i - 1] = key[i][j]
    
    return new_key

def check(a_lock):
    n = len(a_lock) // 3
    
    for i in range(n, 2 * n):
        for j in range(n, 2 * n):
            if a_lock[i][j] != 1:
                return False
    
    return True
    
def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]
            
    for _ in range(4):              
        key = turn_left(key)
        
        for i in range(2 * n):
            for j in range(2 * n):
                a_lock = copy.deepcopy(new_lock)
                for p in range(m):
                    for q in range(m):
                        a_lock[i + p][j + q] += key[p][q] 
                
                if check(a_lock) == True:
                    return True
    
    return False