tc=int(input())
for _ in range(tc):
    n=int(input())
    query=input()
    if query.startswith("A"):
        print("No")
        continue
    counter = 0
    for elem in query:
        if elem == "Q":
            counter-=1
        else:
            counter+=1
    print("Yes" if counter >= 0 else "No")