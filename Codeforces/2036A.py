tc = int(input())
for __ in range(tc):
    n = int(input())
    melody = list(map(int,input().split()))
    ans = True
    for i in range(n-1):
        if abs(melody[i] - melody[i + 1]) == 5 or abs(melody[i] - melody[i + 1]) == 7:
            continue
        else:
            ans = False
            break
    if ans:
        print("YES")
    else:
        print("NO")