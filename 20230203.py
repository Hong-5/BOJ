# Q.11328
N = int(input())

for i in range(N):
    a,b = input().split()
    a = ''.join(sorted(a))
    b = ''.join(sorted(b))
    if a == b:
        print('Possible')
    else:
        print('Impossible')


# Q.1919
from collections import defaultdict

a = input()
b = input()

dict_a = defaultdict(int)
dict_b = defaultdict(int)

for i in a:
    dict_a[i] += 1

for i in b:
    dict_b[i] += 1

cnt = 0
for i in dict_a:
    if i in set(dict_a).intersection(set(dict_b)):
        pass
    else:
        cnt += dict_a[i]

for i in dict_b:
    if i in set(dict_a).intersection(set(dict_b)):
        pass
    else:
        cnt += dict_b[i]

for i in set(dict_a).intersection(set(dict_b)):
    cnt += max(dict_a[i], dict_b[i]) - min(dict_a[i], dict_b[i])

print(cnt)


# Q.2563
num_list = []
cnt = 0
for i in range(9):
    input_num = int(input())
    num_list.append(input_num)

for index, value in enumerate(num_list):
    if value == max(num_list):
        print(value)
        print(index+1)