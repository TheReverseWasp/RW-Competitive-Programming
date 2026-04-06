for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    redto = a[n-1]
    blueto = a[0] + a[1]
    blue_pos = 2
    red_pos = n - 2
    while redto <= blueto and blue_pos < red_pos:
        redto += a[red_pos]
        red_pos -=1
        blueto += a[blue_pos]
        blue_pos += 1
    if redto > blueto:
        print("YES")
    else:
        print("NO")