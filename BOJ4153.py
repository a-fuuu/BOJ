#직각삼각형
import sys
while True:
    a, b, c = map(int,sys.stdin.readline().split())
    if a==b==c==0:
        break
    else:
        lst = [a, b, c]
        mx = max(lst)
        lst.remove(mx)
        if lst[0]**2 + lst[1]**2 == mx**2:
            print("right")
        else:
            print("wrong")