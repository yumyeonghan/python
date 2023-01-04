# 볼링공 고르기
from itertools import combinations

n, m = map(int, input().split())
data = list(map(int, input().split()))
count = 0

for i in list(combinations(data, 2)):
    if i[0] != i[1]:
        count += 1

print(count)