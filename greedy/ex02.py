# 곱하기 혹은 더하기
number = input()
result = int(number[0])

for i in range(1, len(number)):
    if result == 0 or int(number[i]) == 0:
        result += int(number[i])
    else:
        result *= int(number[i])

print(result)
    