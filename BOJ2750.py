# 수 정렬하기
import sys
N = int(sys.stdin.readline())
lst = []
for i in range(N):
    lst.append(int(sys.stdin.readline()))

def bubble(list, len):
    for i in range(len-1,0,-1):
        for j in range(i):
            if list[j] > list[j+1]:
                tmp = list[j+1]
                list[j+1] = list[j]
                list[j]   = tmp
    return list

result = bubble(lst, N)
for x in result:
    print(x)