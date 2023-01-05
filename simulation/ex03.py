# 문자열 재정렬
s = list(input())
s.sort()
report = []
sum = 0

for i in range(len(s)):
    if s[i].isdigit() == True:
        sum += int(s[i])
        report.append(i)

for n in report:
    s.pop(0)

s.append(str(sum))
result = "".join(s)
print(result)