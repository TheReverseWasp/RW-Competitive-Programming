pi = "3141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067"
tc = int(input())
for __ in range(tc):
    i = 0
    Paul = input()
    for elem in Paul:
        if elem == pi[i]:
            i += 1
        else:
            break
    print(i)