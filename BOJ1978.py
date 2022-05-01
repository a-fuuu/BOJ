# 소수찾기
N = int(input())
lst = [int(x) for x in input().split(" ")]
cnt = 0
for _ in range(0,N):
    num = lst.pop()
    div = 2
    while True:
        if num == 1:
            break
        elif num == div:
            cnt += 1
            break
        elif num % div == 0:
            break
        else:
            div += 1
print(cnt)