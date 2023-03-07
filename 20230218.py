# 10828
import sys

try_count = int(sys.stdin.readline())

stack = []


for i in range(try_count):
    tmp = sys.stdin.readline().split()
    if tmp[0] == 'push':
        stack.append(tmp[1])
    elif tmp[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif tmp[0] == 'size':
        print(len(stack))
    elif tmp[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)


# 10773
import sys

stack = []

N = int(sys.stdin.readline())

for i in range(N):
    tmp =  int(sys.stdin.readline())
    if tmp != 0:
        stack.append(tmp)
    else:
        stack.pop()

print(sum(stack))


