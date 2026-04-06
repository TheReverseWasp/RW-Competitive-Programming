tc = int(input())
for __ in range(tc):
    hands = [int(input())]
    nexto = list(map(int,input().split()))
    opened = nexto[hands[0]-1]
    while opened != 0:
        hands.append(opened + 0)
        opened = nexto[hands[-1]-1]
    if len(hands) == 3:
        print("YES")
    else:
        print("NO")