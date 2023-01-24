# 경쟁적 전염(bfs)
from collections import deque

n, k = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
s, x, y = map(int, input().split())

빈칸_수 = 0
virus = []
for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            virus.append((1, 0, i, j))
        if data[i][j] == 2:
            virus.append((2, 0, i, j))
        if data[i][j] == 3:
            virus.append((3, 0, i, j))

virus.sort()
q = deque()

print(virus)

for i in virus:
    q.append(i)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    
    

    종류, time, 행, 열 = q.popleft()
    if time == s:
        break
    
    for i in range(4):
        nx = 행 + dx[i]
        ny = 열 + dy[i]
    
        if 0 <= nx < n and 0 <= ny < n and data[nx][ny] == 0:
            data[nx][ny] = 종류
            q.append((종류, time + 1, nx, ny))

print(data[x - 1][y - 1])
