# 연구소(dfs)
from itertools import combinations
import copy

n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

answer = -1e9
walls = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            walls.append((i, j))

def set_up(wall, new_graph):
    for a, b in wall:
        new_graph[a][b] = 1

def dfs(x, y, new_graph):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if new_graph[nx][ny] == 0:
                new_graph[nx][ny] = 2
                dfs(nx, ny, new_graph)


for wall in list(combinations(walls, 3)):
    new_graph = copy.deepcopy(graph)
    set_up(wall, new_graph)
    count = 0
    
    for i in range(n):
        for j in range(m):
            if new_graph[i][j] == 2:
                dfs(i, j, new_graph)
    
    for i in range(n):
        for j in range(m):
            if new_graph[i][j] == 0:
                count += 1
    
    answer = max(answer, count)

print(answer)