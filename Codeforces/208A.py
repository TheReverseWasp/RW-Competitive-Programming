dbstp = input()
i = 0
ans = ""
while i < len(dbstp):
    if dbstp[i:i+3] == "WUB":
        i+=3
    else:
        temp = i + 1
        for j in range(temp, len(dbstp) + 1):
            temp = j + 0
            if dbstp[j:j+3] == "WUB":
                break
        ans += dbstp[i:temp] + " "
        i = temp + 0
print(ans)