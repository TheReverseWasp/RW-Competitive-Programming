n = int(input())
s = input()
state = 2
for i in range(1,n):
    t = input()
    if state == 2:
        if t < s:
            state = -1
        elif t > s:
            state = 1
    elif state == -1:
        if t > s:
            print("NEITHER")
            state = 0
            break
    elif state == 1:
        if t < s:
            print("NEITHER")
            state = 0
            break
    s = t
if state == 1:
    print("INCREASING")
elif state == -1:
    print("DECREASING")

            