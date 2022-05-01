# 소수 구하기
M, N = [int(x) for x in input().split(" ")]
num_list= list(range(2, N+1))
mini = min(num_list)
div = 2
sosu_lst = []
while div < N**(1/2) + 1:
    num_list = [x for x in num_list if (x % div != 0)]
    sosu_lst.append(div)
    try:
        div = min(num_list)
    except:
        break
res = sosu_lst + num_list
a = [x for x in res if x >= M]
for i in range(0, len(a)):
    print(a[i])


# 1이 있다면 지운다
# 2를 제외한 2로 나뉘는 모든 수 제거
# 3을 제외한 3으로 나뉘는 모든 수 제거
# 그다음부터 존재하는 수 제외하고 그 수로 나뉘는 수 제거