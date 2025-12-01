tc = int(input())
for _ in range(tc):
    a, b = map(int,input().split())
    if (a + b) % 2 == 0:
        print("Tonya")
    else:
        print("Burenka")