tc = int(input())
for __ in range(tc):
    x_ini, y_ini, x_fin, y_fin = map(int,input().split())
    dist_y = y_fin - y_ini
    dist_x = x_fin - x_ini
    if dist_y < 0:
        print(-1)
        continue
    else:
        ans = dist_y
        x_ini += dist_y
        y_ini += dist_y
        if x_ini < x_fin:
            print(-1)
            continue
        else:
            ans += abs(x_ini - x_fin)
            print(ans)