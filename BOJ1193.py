# 분수찾기
x = int(input())
n = 1
z = 2
while x > n:
    n += z
    z += 1
z -= 1
y = n - z
bunmo = x - y
bunza = z - bunmo + 1
if z % 2 == 0 :
    print(f"{bunmo}/{bunza}")
else:
    print(f"{bunza}/{bunmo}")

