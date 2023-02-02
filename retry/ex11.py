# 연산자 끼워 넣기

n = int(input())
data = list(map(int,input().split()))
cal = list(map(int,input().split()))

max_number = -1e9
min_number = 1e9

def dfs(depth, value, p, m, mu, d):

    global max_number, min_number

    if depth == n:
        max_number = max(value, max_number)
        min_number = min(value, min_number)
        return
    
    if p > 0:
        dfs(depth + 1, value + data[depth], p - 1, m, mu, d)
    if m > 0:
        dfs(depth + 1, value - data[depth], p, m - 1, mu, d)
    if mu > 0:
        dfs(depth + 1, value * data[depth], p, m, mu - 1, d)
    if d > 0:
        dfs(depth + 1, int(value / data[depth]), p, m, mu, d - 1)

dfs(1, data[0], cal[0], cal[1], cal[2], cal[3])

print(max_number)
print(min_number)