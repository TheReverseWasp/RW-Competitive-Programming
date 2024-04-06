from copy import copy

def calc_wins(l, pos):
    new_l = list()
    wins = 0
    lose = False
    new_pos = ""
    while not lose and len(l) != 1:
        for i in range(0, len(l) - 1, 2):
            new_l.append(max(l[i], l[i + 1]))
            if i == pos:
                if l[pos] < l[pos + 1]:
                    lose = True
                    break
                else:
                    new_pos = i // 2
                    wins += 1
            elif i + 1 == pos:
                if l[i] > l[pos]:
                    lose = True
                    break
                else:
                    new_pos = i // 2
                    wins += 1
        l = new_l
        pos = new_pos
    return wins

t = int(input())
for i in range(t):
    n, pos = map(int, input().split())
    l = list(map(int, input().split()))
    pos-=1
    if max(l) == l[pos]:
        print(calc_wins(l))
    else:
        maxy = 0
        maxy_idx = 0
        miny = 0
        miny_idx = 0

        for i in range(n):
            if l[i] >= maxy:
                maxy = l[i]
                maxy_idx = i
            if l[i] <= miny:
                miny = l[y]
                miny_idx = i
        left = copy(l)
        rigth = copy(l)
        left[pos], left[maxy_idx] = left[maxy_idx], left[pos]
        rigth[pos], rigth[miny_idx] = rigth[miny_idx], rigth[pos]
        print(max([calc_wins(l,pos), calc_wins(left, maxy_idx), calc_wins(rigth, miny_idx)]))