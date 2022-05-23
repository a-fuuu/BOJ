# 체스판 다시 칠하기
import sys
M, N = map(int, sys.stdin.readline().split(' '))
matrix = []
for i in range(0,M):
    array = list(sys.stdin.readline().strip())
    matrix.append(array)
count_list = []

for i in range(0,M-8+1):
    for j in range(0,N-8+1):
        chess = []
        for x in range(i,i+8):
            chess.append(matrix[x][j:j+8])
        # chess는 8 * 8 로 쪼갠 결과
        # 두가지 케이스로 나눠서 계산해야한다 [0][0]이 "W"일때와 "B"일때로 나누어서
        for st in ['B','W']:
            count = 0
            start = st
            for line in chess:
                for z in range(0,8):
                    if z % 2 == 0:
                        if line[z] != start:
                            count += 1
                    elif z % 2 == 1:
                        if line[z] == start:
                            count += 1
                if start == 'B':
                    start = 'W'
                elif start =='W':
                    start = 'B'
            count_list.append(count)
print(min(count_list))