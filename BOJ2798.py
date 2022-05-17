# blackjack
import sys
N, M = map(int,sys.stdin.readline().split(" "))
num_list = [int(x) for x in sys.stdin.readline().split(" ")]
candidate = []
for i in range(0,len(num_list)):
    for j in range(i+1,len(num_list)):
        for k in range(j+1,len(num_list)):
            num_sum = num_list[i] + num_list[j] + num_list[k]
            if num_sum <= M:
                candidate.append(num_sum)
print(max(candidate))