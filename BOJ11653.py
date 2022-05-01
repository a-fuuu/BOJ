# 소인수분해
N = int(input())
div = 2
if N == 1:
    print()
else:
    while True:
        if N % div == 0:
            N = N / div
            print(div)
        elif N == 1:
            break
        else:
            div += 1