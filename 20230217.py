# 1158
from collections import deque

base_list = []

tmp = list(input().split())

range_num = int(tmp[0])
target_num = int(tmp[1])

for i in range(range_num):
    base_list.append(i+1)

base_list = deque(base_list)

target_len = len(base_list)

final_list = []

cnt = 1

while len(final_list) != range_num:
    if cnt != target_num:
        cnt += 1
        tmp = base_list.popleft()
        base_list.append(tmp)
    else:
        final_list.append(str(base_list.popleft()))
        cnt = 1

print('<'+ ', '.join(final_list) + '>')


# 5397
from collections import deque

password_count = int(input())

for i in range(password_count):
    password = input()
    
    left_cursor = deque()
    right_cursor = deque()
    
    for tmp in password:
        try:
            if tmp == '<':
                right_cursor.appendleft(left_cursor.pop())
            elif tmp == '>':
                left_cursor.append(right_cursor.popleft())
            elif tmp == '-':
                left_cursor.pop()
            else:
                left_cursor.append(tmp)
        except:
            pass
    
    print(''.join(list(list(left_cursor) + list(right_cursor))))