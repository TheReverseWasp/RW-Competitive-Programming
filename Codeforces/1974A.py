tc = int(input())
for __ in range(tc):
    one, two = map(int,input().split())
    current_screen = 0
    size = 15
    while one > 0 or two > 0:
        if two >= 2:
            size -= 8
            two -= 2
        elif two == 1:
            size -= 4
            two = 0
        one -= min(one, size)
        current_screen += 1
        size = 15
    print(current_screen)