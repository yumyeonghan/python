# 뱀
import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
graph = [[0] * (n + 2) for _ in range(n + 2)]

k = int(sys.stdin.readline().rstrip())
apple_graph = []

for _  in range(k):
    apple_graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

for a, b in apple_graph:
    graph[a][b] = 2 #사과가 위치함

l = sys.stdin.readline().rstrip()
snake_direction = []

for _ in range(l):
    a, b = sys.stdin.readline().rstrip().split()
    snake_direction.append(list(int(a), b))

q = deque()
q.append((1, 1))
lenth = 1
graph[1][1] = 1 #뱀이 위치함
direction = 0
time = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while q:
    x, y = q.popleft()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if 1 <= nx <= n and 1 <= ny <= n and graph[nx][ny] != 1:
        lenth += 1
        
        if graph[nx][ny] == 2:
            graph[nx][ny] = 1
                

        
