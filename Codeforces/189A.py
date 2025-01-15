n,a,b,c = map(int,input().split())

l = [-1] * 4001
l[0] = 0
def find_pos(pos):
    if pos < 0:
        return -9999999999
    if l[pos] != -1:
        return l[pos]
    l[pos] = max([find_pos(pos-a), find_pos(pos-b), find_pos(pos-c)]) + 1
    return l[pos]
for i in range(n+1):
    find_pos(i)
print(find_pos(n))