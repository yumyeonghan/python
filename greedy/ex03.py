# 문자열 뒤집기
s = input()

first_value = s[0]
기준 = 1
반대 = 0

현재 = 1 # 기준은 1 반대는 0

for i in range(1, len(s)):
    if s[i] != first_value:
        if 현재 == 1:
            반대 += 1
            현재 = 0
        else:
            기준 += 1
            현재 = 1
        
        first_value = s[i]

print(min(기준, 반대))