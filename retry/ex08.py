# 연구소
from itertools import combinations
import copy

n, m = map(int, input().split())
graph = []
answer = -1e9

for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(new_graph, x, y):
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and new_graph[nx][ny] == 0:
            new_graph[nx][ny] = 2
            dfs(new_graph, nx, ny)

wall_pos = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            wall_pos.append((i, j))

for wall in list(combinations(wall_pos, 3)):
    new_graph = copy.deepcopy(graph)
    count = 0
    for x, y in wall:
        new_graph[x][y] = 1
    
    for i in range(n):
        for j in range(m):
            if new_graph[i][j] == 2:
                dfs(new_graph, i, j)

    for i in range(n):
        for j in range(m):
            if new_graph[i][j] == 0:
                count += 1
    answer = max(count, answer)

print(answer)