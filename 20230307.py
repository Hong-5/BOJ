# Q.1874
N = int(input())

suyeol = []
answer = []

cnt = 1
for i in range(N):
    num = int(input())
    while cnt <= num:
        suyeol.append(cnt)
        answer.append('+')
        cnt += 1

    if suyeol.pop() == num:
        answer.append('-')
    else:
        answer = ['NO']
        break

for i in answer:
    print(i)