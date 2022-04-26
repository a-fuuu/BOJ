# 손익분기점
A, B, C = [int(x) for x in input().split(" ")]
n = 1
if B >= C:
    print(-1)
else:
    D = C - B
    print(int(A / D + 1))