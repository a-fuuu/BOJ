# 벌집
# 1 7 19 37 61
# 6 12 18 24 6의 배수만큼 늘어나는 수열
x = int(input())
n = 0
z = 1
if x == 1:
    print(1)
else :
    while x > z :
        n += 1
        z += 6 * n
    print(n + 1)