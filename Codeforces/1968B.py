def subsequence(a,b):
    ia,posb = 0,0
    while ia < len(a) and posb < len(b):
        if a[ia] == b[posb]:
            ia+=1
        posb+=1
    if ia==len(a):
        return True
    return False

def bin_search(a,b):
    ini = 0
    fin = len(a)
    mid = (ini + fin) // 2
    while ini != fin:
        if subsequence(a[:mid],b):
            ini = mid
        else:
            fin = mid-1
        mid = (ini + fin) // 2 + (1 if (ini + fin) % 2 == 1 else 0)
    return ini
t=int(input())
for __ in range(t):
    n,m=map(int,input().split())
    a=input()
    b=input()
    print(bin_search(a,b))
            