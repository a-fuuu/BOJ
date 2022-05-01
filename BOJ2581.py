# 소수
def sosu_finder(M, N):
    num_list = list(range(M, N+1))
    sosu_lst = []
    for _ in range(0, len(num_list)):
        num = num_list.pop()
        div = 2
        while True:
            if num == 1:
                break
            elif num == div:
                sosu_lst.append(num)
                break
            elif num % div == 0:
                break
            else:
                div += 1
    if not sosu_lst:
        print(-1)
    else:
        print(sum(sosu_lst))
        print(min(sosu_lst))
a = int(input())
b = int(input())
sosu_finder(a, b)