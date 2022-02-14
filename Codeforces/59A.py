def main():
    w = input()
    u, l = 0, 0
    for i in w:
        if i.isupper():
            u += 1
        else:
            l += 1
    if u > l:
        print(w.upper())
    else:
        print(w.lower())

if __name__ == "__main__":
    main()
