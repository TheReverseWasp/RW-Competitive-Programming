tc = int(input())
for i in range(tc):
    a, b = map(int, input().split())
    if a % b == 0:
        print(0)
        continue
    temp = a // b + 1
    temp = temp * b
    print(temp-a)