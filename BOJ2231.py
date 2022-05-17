
import sys
num = int(sys.stdin.readline())
lst = []
for i in range(0,num):
    num_lst = [int(x) for x in list(str(i))]
    if i + sum(num_lst) == num:
        lst.append(i)
if lst != []:
    print(min(lst))
else:
    print(0)