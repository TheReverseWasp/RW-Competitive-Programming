
def gen_seq(l):
    left, right = [], []
    it = 0
    ini, end = 0, len(l)-1
    while it < len(l) - 1:
        if l[ini] < l[end]:
            left.append(l[ini])
            ini += 1
        else:
            right.append(l[end])
            end -= 1
        it += 1
    left = [left[i] for i in range(len(left) - 1, -1, -1)]
    return left + right + [l[end]], [l[end]] + left + right

def same_as(l1, l2):
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            return False
    return True

t = int(input())
while t:
    t-=1
    n = int(input())
    l = list(map(int,input().split()))
    pos1, pos2 = gen_seq(l)
    ans = [pos1, pos2]
    (posa, posb), (posc, posd) = (gen_seq(pos1)), (gen_seq(pos2))
    posible = [posa, posb, posc, posd]
    temp = [True,True,True,True,]
    for i in range(len(posible)):
        if same_as(posible[i], l):
            print(" ".join([str(elem) for elem in ans[int(i/2)]]))
            break
        else:
            temp[i] = False
    if temp[-1] == False:
        print(-1)
