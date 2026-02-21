for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    if len(set(a)) == 1:
        print("NO")
        continue
    ans = ""
    db = set()
    already_blue = False
    for elem in a:
        if not already_blue:
            if elem in db:
                already_blue = True
                ans+="B"
            else:
                ans+="R"
                db.add(elem)
        else:
            ans+="R"
    if not already_blue:
        ans = ans[:-1] + "B"
    print("YES")
    print(ans)