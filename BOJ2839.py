# 설탕 배달

N = int(input())
# cnt = 0
# lst = [3, 5]
# if N % 15 == 0:
#     print(int(N / 5))
# elif N % 5 == 0:
#     print(int(N / 5))
# else:
#     while True:
#         new_lst = []
#         for i in range(0, len(lst)):
#             for j in [3, 5]:
#                 new_lst.append(j + lst[i])
#         cnt += 1
#         if N in lst:
#             print(cnt)
#             break
#         elif N < min(lst):
#             print(-1)
#             break
#         else:
#             lst = list(set(new_lst))
cnt = 0
while True:
    if N >= 5 and N % 5 == 0:
        print(int(cnt + N / 5))
        break
    elif N >= 3:
        N -= 3
        cnt += 1
    elif N == 0:
        print(cnt)
        break
    else:
        print(-1)
        break