# 수 정렬하기 2
import sys
N = int(sys.stdin.readline())
lst = []
for i in range(N):
    lst.append(int(sys.stdin.readline()))
lst.sort()
for x in lst:
    print(x)