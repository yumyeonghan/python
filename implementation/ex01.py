# 게임 개발(시뮬레이션)
n, m = map(int,input().split())
x, y, direction = map(int, input().split())
data = []
for _ in range(m):
    data.append(list(map(int, input().split())))

data[x][y] = 1
count = 1
turn_time = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left(direction):
    index = direction - 1
    if index == -1:
        index = 3
    return index

while True:
    direction = turn_left(direction)
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    if data[nx][ny] != 1:
        x = nx
        y = ny
        data[x][y] = 1
        count += 1
        turn_time = 0
        continue
    
    else:
        turn_time += 1
    
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if data[nx][ny] != 1:
            x = nx
            y = ny
            data[x][y]
            count+= 1
            turn_time = 0
            continue
        else:
            break

print(count)