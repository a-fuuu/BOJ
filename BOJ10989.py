# 스택
import sys

n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    select = sys.stdin.readline().strip()

    if 'push' in select:
        num = int(select.split(' ')[1])
        stack.append(num)
    elif select == 'pop':
        if stack:
            num = stack[-1]
            print(num)
            del (stack[-1])
        else:
            print(-1)
    elif select == 'size':
        print(len(stack))
    elif select == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif select == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)