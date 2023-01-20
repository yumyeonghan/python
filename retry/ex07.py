# 특정 거리의 도시 찾기
import sys
from collections import deque

n, m, k , x = map(int, sys.stdin.readline().rstrip().split())
distance = [-1] * (n + 1)
distance[x] = 0
city = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    city[a].append(b)

next_city = deque()
next_city.append(x)

while next_city:
    current_position = next_city.popleft()
    city_inf = city[current_position]

    for inf in city_inf:
        if distance[inf] == -1:
            distance[inf] = distance[current_position] + 1
            next_city.append(inf)

answer = []

for i in range(1, n + 1):
    if distance[i] == k:
        answer.append(i)

if answer:
    for result in answer:
        print(result)
else:
    print(-1)