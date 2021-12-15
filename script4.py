globalist = ['1']
lst = [globalist]
n = int(input())
if  1 <= n <= 100:
    for i in range (n):
        cmd, namesp, arg = input().split()
else:
    print('Out of range')
