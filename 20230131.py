# Q. 10871
import sys

n,m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))


for i in arr:
    if i < m:
        print(i)


# Q. 1000
import sys

n,m = map(int, sys.stdin.readline().split())

print(n+m)


# Q. 2309
from itertools import combinations

small_list = []

for i in range(9):
    small_list.append(int(input()))

for i in list(combinations(small_list, 7)):
    if sum(i) == 100:
        nan_list = list(sorted(i))
        for i in nan_list:
            print(i)
        break

# Q. 2490
arr = []
for _ in range(3): # m번 loop을 돌면서 input을 arr에 append
	arr.append(list(map(int, input().split())))

for turn in arr:
    if turn.count(0) == 1:
        print('A')
    elif turn.count(0) == 2:
        print('B')
    elif turn.count(0) == 3:
        print('C')
    elif turn.count(0) == 4:
        print('D')
    else:
        print('E')


