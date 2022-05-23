# 체스판 다시 칠하기
import sys
M, N = map(int, sys.stdin.readline().split(' '))
matrix = []
for i in range(0,M):
    array = list(sys.stdin.readline())
    matrix.append(array)
count_list = []
for i in range(0,M-8+1):
    for j in range(0,N-8+1):
        chess = []
        for x in range(i,i+8):
            chess.append(matrix[x][j:j+8])
        print(chess)
        count = 0
        start = chess[0][0]
        for line in chess:
            for i in range(1,8):
                line[0] = start
                if line[i] == line[i-1]:
                    if line[i-1] == "B":
                        line[i] = "W"
                        count += 1
                    else:
                        line[i] = "B"
                        count += 1
            if start == "B":
                strat = "W"
            elif start =="W":
                start = "B"
        count_list.append(count)
print(count_list)