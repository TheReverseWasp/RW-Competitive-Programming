tc = int(input())
for __ in range(tc):
    a,b = map(int,input().split())
    ans = a+b
    if ans % 2 == 0:
        print("Bob")
    else:
        print("Alice")