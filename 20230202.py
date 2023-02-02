# Q.10804
order_list = []
for i in range(10):
    a, b = map(int, input().split())
    order_list.append([a,b])
    
base_list = [i for i in range(1,21)]

for a in order_list:
    base_list = base_list[:a[0]-1] + base_list[a[0]-1:a[1]][::-1] + base_list[a[1]:]
    
print(' '.join(list(map(str, base_list))))


# Q.15552 
import sys

T = int(input())

for i in range(T):
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)


# Q. 별그리기 -> 너무기본이라 하나만

N = int(input())

for i in range(N):
    print((" ")*i +"*"*(N-i))


# Q.10807 
import sys

N = int(input())
num_list = list(map(int, sys.stdin.readline().split()))
find_num = int(input())
print(num_list.count(find_num))


# Q.13300

from collections import defaultdict

N, K = map(int, input().split())

room_dict = defaultdict(int)

for i in range(N):
    sex, grade = input().split()
    room_dict[sex+grade] += 1

cnt = 0
for i in room_dict:
    if room_dict[i] % 2 == 0:
        cnt += room_dict[i] // K
    else:
        cnt += room_dict[i] // K + 1

print(cnt)

