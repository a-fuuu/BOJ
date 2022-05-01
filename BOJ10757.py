a, b = input().split(" ")
a_list = list(a)
b_list = list(b)
new_list = []
ten = 0
while True:
    try:
        x = int(a_list[-1]) + int(b_list[-1]) + ten
        if x >= 10:
            new_list.append(str(x - 10))
            ten = 1
            a_list.pop()
            b_list.pop()
        else:
            new_list.append(str(x))
            ten = 0
            a_list.pop()
            b_list.pop()
    except:
        if (a_list == b_list == []) and ten == 0:
            break
        elif (a_list == b_list == []) and ten == 1:
            new_list.append(str(ten))
            break
        elif a_list == []:
            final = b_list
            a = len(final)
            for i in range(0, len(final)):
                y = int(final.pop()) + ten
                if y >= 10:
                    new_list.append(str(y - 10))
                    ten = 1
                else:
                    new_list.append(str(y))
                    ten = 0
                if i == a - 1:
                    if ten == 1:
                        new_list.append(str(ten))
            break
        elif b_list == []:
            final = a_list
            a = len(final)
            for i in range(0, len(final)):
                y = int(final.pop()) + ten
                if y >= 10:
                    new_list.append(str(y - 10))
                    ten = 1
                else:
                    new_list.append(str(y))
                    ten = 0
                if i == a - 1:
                    if ten == 1:
                        new_list.append(str(ten))
            break
val = ""
while True:
    try:
        val += new_list.pop()
    except:
        print(val)
        break