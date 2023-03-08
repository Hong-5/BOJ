# Q. 10845

from sys import stdin

N = int(stdin.readline())

tmp_list = []

for i in range(N):
    tmp = stdin.readline().split()
    if tmp[0] == 'push':
        tmp_list.append(tmp[1])
    elif tmp[0] == 'pop':
        if len(tmp_list) != 0:
            print(tmp_list.pop(0))
        else:
            print(-1)
    elif tmp[0] == 'size':
        print(len(tmp_list))
    elif tmp[0] == 'empty':
        if len(tmp_list) != 0:
            print(0)
        else:
            print(1)
    elif tmp[0] == 'front':
        if len(tmp_list) != 0:
            print(tmp_list[0])
        else:
            print(-1)
    elif tmp[0] == 'back':
        if len(tmp_list) != 0:
            print(tmp_list[-1])
        else:
            print(-1)


# Q. 18258

from collections import deque
from sys import stdin

N = int(stdin.readline())

tmp_list = deque()

for i in range(N):
    tmp = stdin.readline().split()
    if tmp[0] == 'push':
        tmp_list.append(tmp[1])
    elif tmp[0] == 'pop':
        if len(tmp_list) != 0:
            print(tmp_list.popleft())
        else:
            print(-1)
    elif tmp[0] == 'size':
        print(len(tmp_list))
    elif tmp[0] == 'empty':
        if len(tmp_list) != 0:
            print(0)
        else:
            print(1)
    elif tmp[0] == 'front':
        if len(tmp_list) != 0:
            print(tmp_list[0])
        else:
            print(-1)
    elif tmp[0] == 'back':
        if len(tmp_list) != 0:
            print(tmp_list[-1])
        else:
            print(-1)