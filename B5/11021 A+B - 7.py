# 11021 A+B - 7
t = int(input())

for i in range(1, t+1):
    a, b = map(int, input().split())
    sum = a+b
    print(f'Case #', i, f': ', sum, sep='')