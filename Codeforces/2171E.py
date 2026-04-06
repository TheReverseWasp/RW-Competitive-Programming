tc = int(input())
for _ in range(tc):
    n = int(input())
    threes = [str(i) for i in range(3,n+1,3)]
    s3 = set(threes)
    twos = list()
    for i in range(2,n+1,2):
        if str(i) not in s3:
            twos.append(str(i))
    s2 = set(twos)
    others = list()
    for i in range(1,n+1):
        if str(i) not in s2 and str(i) not in s3:
            others.append(str(i))
    ans = list()
    others_idx = 0
    twos_idx = 0
    threes_idx = 0
    runner = 0
    while len(ans) < n:
        if others_idx < len(others):
            ans.append(others[others_idx])
            others_idx+=1
        if twos_idx < len(twos):
            if len(twos) - twos_idx == 1:
                ans.append(twos[twos_idx])
                twos_idx+=1
            else:
                ans.append(twos[twos_idx])
                twos_idx+=1
                ans.append(twos[twos_idx])
                twos_idx+=1
        elif threes_idx < len(threes):
            if len(threes) - threes_idx == 1:
                ans.append(threes[threes_idx])
                threes_idx+=1
            else:
                ans.append(threes[threes_idx])
                threes_idx+=1
                ans.append(threes[threes_idx])
                threes_idx+=1
    print(" ".join(ans))


