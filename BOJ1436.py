# 영화감독 숌
import sys

sixnum_list = []
N = int(sys.stdin.readline())

def sixsixsix(num):
    num_to_str = str(num)
    
    if '666' in num_to_str :
        return True

i = 666

while len(sixnum_list) < N:
    if sixsixsix(i):
        sixnum_list.append(i)
    i += 1

print(sixnum_list[-1])