tc = int(input())
for __ in range(tc):
    input()
    road = input()
    actual = (0,0)
    for direction in road:
        if direction == "U":
            actual = (actual[0], actual[1] + 1)
        elif direction == "D":
            actual = (actual[0], actual[1] -1)
        elif direction == "L":
            actual = (actual[0] - 1, actual[1])
        else:
            actual = (actual[0] + 1, actual[1])
        if actual == (1,1):
            break
    if actual == (1,1):
        print("YES")
    else:
        print("NO")