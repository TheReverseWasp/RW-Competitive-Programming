n,t = map(int,input().split())
books = list(map(int,input().split()))
cum_books = [0]
for elem in books:
    cum_books.append(cum_books[-1] + elem)

def bin_search(ini, fin, true_ini):
    if ini == fin:
        return ini
    half = (ini + fin) // 2
    if cum_books[half] - cum_books[true_ini - 1] > t:
        return bin_search(ini, half, true_ini)
    else:
        return bin_search(half + 1, fin, true_ini)

ans = 0
for i in range(1, n + 1):
    ans = max(ans, bin_search(i,n + 1,i) - i)
print(ans)