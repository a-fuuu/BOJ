import sys
num_list = list(range(2,10001))
div = 2
div_list = []
while div <= 100:
    num_list = [x for x in num_list if x % div != 0]
    div_list.append(div)
    div = num_list[0]
sosu = div_list + num_list

def goldbach(x):
    lst = [a for a in sosu if a <= x*(1/2)]
    for i in range(1,len(lst) + 1):
        a = lst[-i]
        if x - a in sosu:
            b = x - a
            break
    return [a, b]
sibal = []
for i in range(4,10001,2):
    sibal.append(goldbach(i))
n = int(sys.stdin.readline())
for _ in range(0,n):
    a = sibal[int(int(sys.stdin.readline())/2)-2]
    print(a[0],a[1])