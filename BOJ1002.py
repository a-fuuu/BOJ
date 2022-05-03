# 터렛
import sys
for i in range(0,int(sys.stdin.readline())):
    x_1, y_1, r_1, x_2, y_2, r_2 = map(int, sys.stdin.readline().split(" "))
    point_to_point = ((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2) ** (1 / 2)
    r = r_1 + r_2
    max_r = max(r_1,r_2)
    min_r = min(r_1,r_2)
    if point_to_point > r:
        print(0)
    elif point_to_point == 0 and r_1 != r_2:
        print(0)
    elif point_to_point == 0 and r_1 == r_2:
        print(-1)
    elif max_r > point_to_point + min_r:
        print(0)
    elif point_to_point == r:
        print(1)
    elif max_r == point_to_point + min_r:
        print(1)
    elif point_to_point < r:
        print(2)