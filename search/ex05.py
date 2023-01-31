# 연산자 끼워 넣기(dfs)
n = int(input())
data = list(map(int, input().split()))
calculate = list(map(int, input().split()))

큰값 = -1e9
작은값 = 1e9

def dfs(depth, value, 더하기, 빼기, 곱셈, 나눗셈):
    global 큰값
    global 작은값

    if depth == n:
        큰값 = max(value, 큰값)
        작은값 = min(value, 작은값)
        return # 브레이크 걸어줘야 n개의 수만 개산한다.

    if 더하기 > 0:
        dfs(depth+1, value + data[depth], 더하기 - 1, 빼기, 곱셈, 나눗셈)
    if 빼기 > 0:
        dfs(depth+1, value - data[depth], 더하기, 빼기 - 1, 곱셈, 나눗셈)
    if 곱셈 > 0:
        dfs(depth+1, value * data[depth], 더하기, 빼기, 곱셈 - 1, 나눗셈)
    if 나눗셈 > 0:
        dfs(depth+1, int(value / data[depth]), 더하기, 빼기, 곱셈, 나눗셈 - 1)

dfs(1, data[0], calculate[0], calculate[1], calculate[2], calculate[3])

print(큰값)
print(작은값)