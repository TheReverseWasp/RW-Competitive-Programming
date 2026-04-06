tc = int(input())
for _ in range(tc):
    n=int(input())
    a=input()
    ans = ""
    binary_anxiety = True
    for elem in a[1:]:
        if elem == "0":
            ans+="+"
        else:
            if binary_anxiety:
                ans+="-"
            else:
                ans+="+"
            binary_anxiety = not binary_anxiety
    print(ans)