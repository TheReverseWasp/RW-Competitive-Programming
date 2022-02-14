def main():
    f = int(input())
    fl = [0, 0, 0]
    for i in range(f):
        l = list(map(int, input().split()))
        for i in range(len(l)):
            fl[i] += l[i]
    for i in fl:
        if i != 0:
            print("NO")
            return
    print("YES")


if __name__ == "__main__":
    main()