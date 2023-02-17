import sys

left_stack = list(sys.stdin.readline().strip())
right_stack = []

cnt = int(input())

for i in range(cnt):
    tmp = sys.stdin.readline().strip()
    if tmp[0] == 'L':
        if len(left_stack) != 0:
            num = left_stack.pop()
            right_stack.append(num)
    elif tmp[0] == 'B':
        if len(left_stack) != 0:
            left_stack.pop()
    elif tmp[0] == 'P':
          left_stack.append(tmp[2])
    else:
        if len(right_stack) != 0:
            num = right_stack.pop()
            left_stack.append(num)

print(''.join(left_stack + list(reversed(right_stack))))