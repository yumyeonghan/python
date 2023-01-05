# 럭키 스트레이트
s = input()

def check(s):
    middle_point = len(s) // 2
    sum_f = 0
    sum_b = 0
    front = s[:middle_point]
    back = s[middle_point:]
    
    for n in front:
        sum_f += int(n)
    for n in back:
        sum_b += int(n)
    
    if sum_f == sum_b:
        print("LUCKY")
    else:
        print("READY")

check(s)