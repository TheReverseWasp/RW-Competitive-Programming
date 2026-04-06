r, b = map(int,input().split())
ans = min([r,b])
print(ans, end=" ")
r-=ans
b-=ans
r += b
ans = r//2
print(ans)