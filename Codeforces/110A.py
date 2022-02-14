def main():
    s = input()
    a = 0
    for i in s:
        if i == "4" or i == "7":
            a += 1
    a = str(a)
    for i in a:
        if i != "4" and i != "7":
            print("NO")
            return 0
    print("YES")

if __name__ == "__main__":
    main()
