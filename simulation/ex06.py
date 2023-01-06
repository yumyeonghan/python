# 뱀
n = int(input())
map_data = [[0] * (n + 1) for _ in range(n + 1)]

k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    map_data[a][b] = 1 # 사과 위치는 1

l = int(input())
snake_inf = []
for _ in range(l):
    t, d = input().split()
    snake_inf.append((int(t), d))

# 동 남 서 북
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def turn(direction, turn_inf):
    if turn_inf == "L":
        result = (direction + 1) % 4
    else:
        result = (direction - 1) % 4
    return result

def simulate():

    x, y = 1, 1
    map_data[x][y] = 2
    direction = 0
    index = 0
    time = 0
    q = [(x, y)]

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 1 <= nx <= n and 1 <= ny <= n and map_data[nx][ny] != 2:
            if map_data[nx][ny] == 0:
                map_data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                map_data[px][py] = 0
            if map_data[nx][ny] == 1:
                map_data[nx][ny] = 2
                q.append((nx, ny))
        else:
            time += 1
            break

        x, y = nx, ny
        time += 1
        
        if index < l and time == snake_inf[index][0]:
            direction = turn(direction, snake_inf[index][1])
            index += 1
    return time

print(simulate())