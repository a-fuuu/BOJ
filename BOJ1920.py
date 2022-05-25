import sys
N = int(sys.stdin.readline())
lst_1 = list(map(int, sys.stdin.readline().split(' ')))
M = int(sys.stdin.readline())
lst_2 = list(map(int, sys.stdin.readline().split(' ')))
lst_1.sort()
def binary(num):
    left = 0
    right = N - 1
    lst = lst_1
    while left <= right:
        mid = (left + right)//2
        if num == lst[mid]:
            return True
        if num < lst[mid]:
            right = mid - 1
        else:
            left = mid + 1
for i in lst_2:
    if binary(i):
        print(1)
    else:
        print(0)