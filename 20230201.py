# Q. 10808


input_str = input()

alpha = 'abcdefghijklmnopqrstuvwxyz'

base_str = ''

for i in alpha:
    num = input_str.count(i)
    base_str += str(num)
    base_str += ' '

print(base_str[:-1])


# Q. 2577

base_num = 1

for i in range(3):
    base_num *= int(input())

base_num = str(base_num)

target_num = '0123456789'

for i in target_num:
    print(base_num.count(i))


# Q. 1475

def plus_1(array):
    for i in range(len(array)):
        array[i] += 1
    return array

from collections import defaultdict

have_to_make=str(input()).rstrip()

num_dict = [0]*10

cnt = 0
tmp = 0

for i in have_to_make:
    if tmp == 0:
        cnt += 1
        plus_1(num_dict)
        num_dict[int(i)] -= 1
    else:
        if num_dict[int(i)] == 0:
            if int(i) == 6:
                if num_dict[9] != 0:
                    num_dict[9] -= 1
                else:
                    cnt += 1
                    plus_1(num_dict) 
                    num_dict[int(i)] -= 1
            elif int(i) == 9:
                if num_dict[6] != 0:
                    num_dict[6] -= 1
                else:
                    cnt += 1
                    plus_1(num_dict)
                    num_dict[int(i)] -= 1
            else:
                cnt += 1
                plus_1(num_dict)
                num_dict[int(i)] -= 1
        else:
            num_dict[int(i)] -= 1
    tmp += 1

print(cnt)


# Q. 3273

# 메모리 초과
from itertools import combinations

N = int(input())

num_list = list(combinations(list(map(int, input().split())),2))   
target_num = int(input())
answer = 0

for i in num_list:
    if sum(i) == target_num:
        answer += 1

print(answer)

# 시간초과 (O(n2))
N = int(input())

num_list = list(map(int, input().split()))
    
target_num = int(input())

answer = 0

for i in num_list:
    if (target_num-i) in num_list:
        answer += 1
    else:
        pass

print(answer/2)

# Two pointer
N = int(input())

num_list = list(map(int, input().split()))

target_num = int(input())

num_list = sorted(num_list)

tmp_list = [0]*(max(target_num,num_list[-1])+1)

cnt = 0

for i in num_list:
    if target_num < i:
        pass
    else:
        if tmp_list[target_num - i] == 1:
            cnt += 1
        else:
            tmp_list[i] = 1
print(cnt)
