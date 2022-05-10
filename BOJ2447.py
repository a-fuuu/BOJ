#별 찍기 - 10
import sys
def star(n):
    star(n/3) star(n/3) star(n/3)
    star(n / 3)
    star(n / 3)
    star(n / 3)

star(int(sys.stdin.readline()))