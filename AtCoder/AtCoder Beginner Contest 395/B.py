n = int(input())
ans = ["#" * n for __ in range(n)]
for i in range(1,n//2 + 1):
    for j in range(i,n-i):
        chad_symbol = "." if ans[j][i-1] == "#" else "#"
        ans[j] = ans[j][:i] + chad_symbol * (n-i*2) + ans[j][-i:]
print("\n".join(ans))
