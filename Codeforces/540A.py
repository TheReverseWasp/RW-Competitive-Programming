n = int(input())
a = input()
b = input()

ans = 0

for i in range(n):
    ans += min([
        abs(int(a[i]) - int(b[i])), 
        abs(int(a[i]) - 10 - int(b[i])),
        abs(int(a[i]) + 10 - int(b[i])), 
        ])
print(ans)
