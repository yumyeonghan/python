# 경쟁적 전염
from collections import deque

n, k = map(int, input().split())
data = []
virus = []
for i in range(n):
    data.append(list(map(int, input().split())))
    for j in range(n):
        if data[i][j] != 0:
            virus.append((data[i][j], 0, i, j))

virus.sort()
q = deque()
for v in virus:
    q.append(v)

s, x, y = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    v, t, px, py = q.popleft()

    if t == s:
        break

    for i in range(4):
        nx = px + dx[i]
        ny = py + dy[i] 
        if 0 <= nx < n and 0 <= ny < n and data[nx][ny] == 0:
            data[nx][ny] = v
            q.append((v, t + 1, nx, ny))

print(data[x - 1][y - 1])