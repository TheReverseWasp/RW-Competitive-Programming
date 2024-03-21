def walk(s1, s2):
    for i in range(len(s1)-1):
        if s1[i:i+2] == "<<" and s2[i:i+2] == "<<":
            return False
    return s2[-2] != "<"

t = int(input())
while t:
    t-=1
    n = input()
    s1 = input()
    s2 = input()
    if walk(s1, s2):
        print("YES")
    else:
        print("NO")