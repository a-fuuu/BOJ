# 베르트랑 공준
import sys
num_lst = list(range(2,2*123456 + 1))
div = 2
sosu_lst = []
while div < (2*123456)**(1/2) + 1:
    try:
        num_lst = [x for x in num_lst if x % div != 0]
        sosu_lst.append(div)
        div = num_lst[0]
    except:
        break
sosu = sosu_lst + num_lst
while True:
    j = int(sys.stdin.readline())
    if j == 0:
        break
    else:
        print(len([x for x in sosu if ( j < x <= 2*j)]))