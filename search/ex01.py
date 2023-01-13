# 특정 거리의 도시 찾기(bfs)
from collections import deque
import sys

n, m, k, x = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n + 1)]
city = [-1] * (n + 1)
city[x] = 0

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)

q = deque()
q.append(x)

while q:
    now = q.popleft()
    for next_x in graph[now]:
        if city[next_x] == -1:
            city[next_x] = city[now] + 1
            q.append(next_x)

check = False
answer = []

for c in range(len(city)):
    if city[c] == k:
        check = True
        answer.append(c)

if answer:
    for a in answer:
        print(a)
else:
    print(-1)