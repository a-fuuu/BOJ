import sys
N = int(sys.stdin.readline())
lst_1 = map(int, sys.stdin.readline().split(' ')).sort()
M = int(sys.stdin.readline())
lst_2 = map(int, sys.stdin.readline().split(' '))

def divtwo()

while lst_2 != []:
    num = lst_2.pop(0)
    if lst_1[len(lst_1)//2] > num:
        