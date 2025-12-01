tc = int(input())
for _ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    fixed = list()
    lasto_parto = list()
    resagados = set()
    for elem in a:
        if not elem in resagados:
            fixed.append(elem)
        else:
            lasto_parto.append(elem)
        resagados.add(elem)
    print(" ".join([str(elem) for elem in fixed+lasto_parto]))