num = int(input())
max_num = num
while num != 0:
    if num > max_num:
        max_num = num
    num = int(input())
print(max_num)