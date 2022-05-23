import sys
N = int(sys.stdin.readline())
w_h_list = []

for i in range(0,N):
    w, h = map(int,sys.stdin.readline().split(" "))
    w_h_list.append([w,h])
rank_list = []
for i in range(0,N):
    pop = w_h_list[i]
    rank = 0
    for j in w_h_list:
        if pop[0] < j[0] and pop[1] < j[1]:
            rank += 1
    rank_list.append(rank+1)

print(*rank_list, sep=' ')