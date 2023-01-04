# 만들 수 없는 금액
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = data[0]

for i in range(1, len(data)):
    if result < data[i]:
        result += 1
        break
    
    result += data[i]

print(result)