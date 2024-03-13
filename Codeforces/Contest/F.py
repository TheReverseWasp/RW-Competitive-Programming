t = int(input())
while t:
    t-=1
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    d = list(map(int, input().split()))
    f = list(map(int, input().split()))
    inbalance = -1
    index_of_hate = -1
    for i in range(n - 1):
        if a[i+1] - a[i] > inbalance:
            inbalance = a[i+1] - a[i]
            index_of_hate = i + 0
    difficulties = set()
    for elem1 in d:
        for elem2 in f:
            difficulties.add(elem1 + elem2)
    difficulties = list(difficulties)
    difficulties.sort()
    k1 = a[index_of_hate]
    k2 = a[index_of_hate + 1]
    def bin_search(min, max, k):
        mid = (min + max) // 2
        if min == max:
            return mid
        if difficulties[mid] > k:
            return bin_search(min, mid, k)
        elif difficulties[mid] < k:
            return bin_search(mid + 1, max, k)
        else:
            return mid
    idx1 = bin_search(0, len(difficulties), k1)
    idx2 = bin_search(0, len(difficulties), k2)
    idx_fixed = (idx1 + idx2) // 2
    if max(difficulties[idx_fixed] - a[index_of_hate],  a[index_of_hate + 1] -difficulties[idx_fixed]) < max(difficulties[idx_fixed + 1] - a[index_of_hate],  a[index_of_hate + 1] -difficulties[idx_fixed + 1]):
        a.insert(index_of_hate + 1, difficulties[idx_fixed])
    else:
        a.insert(index_of_hate + 1, difficulties[idx_fixed + 1])
    
    inbalance_2 = -1
    for i in range(len(a) - 1):
        if a[i+1] - a[i] > inbalance_2:
            inbalance_2 = a[i+1] - a[i]

    print(min(inbalance_2, inbalance))