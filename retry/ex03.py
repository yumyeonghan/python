# 자물쇠와 열쇠
import copy

def turn(key):
    n = len(key)
    new_key = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            new_key[n - j - 1][i] = key[i][j]
    return new_key

def check(new_lock):
    n = len(new_lock)
    
    for i in range(n // 3):
        for j in range(n // 3):
            if new_lock[i + n//3][j + n//3] != 1:
                return False
    return True

def solution(key, lock):
    
    n = len(lock)
    m = len(key)
    new_lock = [[0] * n * 3 for _ in range(n * 3)]
    
    for i in range(n):
        for j in range(n):
            new_lock[n + i][n + j] = lock[i][j]

    for _ in range(4):
        key = turn(key)
        
        for i in range(n * 2):
            for j in range(n * 2):
                new_lock_2 = copy.deepcopy(new_lock)
                
                for p in range(m):
                    for q in range(m):
                        new_lock_2[i + p][j + q] = new_lock_2[i + p][j + q] + key[p][q] 
                
                if check(new_lock_2):
                    return True
    return False