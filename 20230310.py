# Q. 6198

N = int(input())

stack = []

answer = 0

for i in range(N):
    building = int(input())
    if len(stack) == 0:
        stack.append(building)
    else:
        while True:
            if len(stack) == 0:
                stack.append(building)
                break
            else:
                if stack[-1] <= building:
                    stack.pop()
                else:
                    answer += len(stack)
                    stack.append(building)
                    break
print(answer)

