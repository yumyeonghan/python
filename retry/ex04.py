# 뱀
import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
graph = [[0] * (n + 1) for _ in range(n + 1)]
k = int(sys.stdin.readline().rstrip())
apple_graph = []

for _  in range(k):
    apple_graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

for a, b in apple_graph:
    graph[a][b] = 2 #사과가 위치함

l = int(sys.stdin.readline().rstrip())
snake_direction = []

for _ in range(l):
    a, b = sys.stdin.readline().rstrip().split()
    snake_direction.append((int(a), b))

q = deque()
q.append((1, 1))
graph[1][1] = 1 #뱀이 위치함
direction = 0
time = 0
index = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
x, y = 1, 1

def turn(direction, c):
    if c == "L":
        answer = (direction - 1) % 4
    else:
        answer = (direction + 1) % 4
    return answer


while q:
    
    nx = x + dx[direction]
    ny = y + dy[direction]

    if 1 <= nx <= n and 1 <= ny <= n and graph[nx][ny] != 1:
        
        if graph[nx][ny] == 2:
            graph[nx][ny] = 1
            q.append((nx, ny))
            x, y = nx, ny
        
        if graph[nx][ny] == 0:
            graph[nx][ny] = 1
            q.append((nx, ny))
            a, b = q.popleft()
            graph[a][b] = 0
            x , y = nx, ny
    
        time += 1
    else:
        time += 1
        break    

    if index < l and time == snake_direction[index][0]:
        direction = turn(direction, snake_direction[index][1])
        index += 1

print(time)