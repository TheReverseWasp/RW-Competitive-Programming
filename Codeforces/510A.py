v, h = map(int, input().split())
for i in range(v):
    if i % 2 == 0:
        print("#" * h)
        continue
    if (i // 2) % 2 == 0:
        print(("." * (h - 1)) + "#")
    else:
        print("#" + ("." * (h-1)))