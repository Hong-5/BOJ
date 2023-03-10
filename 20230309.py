from collections import deque
from sys import stdin

N = int(stdin.readline())
que = deque()

if N != 1:
    for i in range(1,N+1):
        que.append(i)
    while len(que) != 2:
        que.popleft()
        que.append(que.popleft())
    print(que[-1])
else:
    print(1)