d_l = input().split()
m = {}
while len(d_l) > 1:
    m[d_l[1]] = d_l[0]
    d_l = input().split()


t = input()
while t[-1] != "":
    if t in m:
        print(m[t])
    else: 
        print("eh")
    t = input()