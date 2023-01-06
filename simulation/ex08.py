#치킨 배달
import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().rstrip().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

person_data = []
store_data = []

for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            person_data.append((i, j))
        if data[i][j] == 2:
            store_data.append((i, j))

store = list(combinations(store_data, m))

result = 1e9

for inf in store:

    city_chicken_distance = 0
    for px, py in person_data:
        chicken_distance = 1e9
        for sx, sy in inf:
            chicken_distance = min(abs(sx - px) + abs(sy - py), chicken_distance)
        city_chicken_distance += chicken_distance
    result = min(result, city_chicken_distance)

print(result)