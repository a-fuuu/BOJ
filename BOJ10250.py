# ACM 호텔
def hotel(width, height, n):
    if n <= width * height:
        if n % height == 0:
            dong = height
            ho = n // height
        else:
            dong = n % height
            ho = n // height + 1
        if ho >= 10:
            print(f"{dong}{ho}")
        else:
            print(f"{dong}0{ho}")
n = int(input())
for i in range(n):
    H, W, N = [int(x) for x in input().split(" ")]
    hotel(W, H, N)