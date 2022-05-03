# 네 번째 점
import sys
a = []
b = []
for i in range(0,3):
    x, y = map(int,sys.stdin.readline().split())
    if x in a:
        a.remove(x)
    else:
        a.append(x)
    if y in b:
        b.remove(y)
    else:
        b.append(y)
print(a[0],b[0])