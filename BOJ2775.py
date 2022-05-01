# 부녀회장이 될테야
def soso(k, h):
    i = 0
    lst = []
    while i != k:
        if i == 0:
            for j in range(1, h+1):
                lst.append(j)
            i += 1
        else:
            new_lst = []
            for x in range(0,h):
                new_lst.append(sum(lst[0:x+1]))
            lst = new_lst
            i += 1
    print(sum(lst[0:h]))

test = int(input())

for i in range(0, test):
    k = int(input())
    h = int(input())
    soso(k, h)