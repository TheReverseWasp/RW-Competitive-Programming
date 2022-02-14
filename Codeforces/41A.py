def main():
    s1 = input()
    s2 = input()
    if len(s1) != len(s2):
        print("NO")
        return 0
    s1 = s1[::-1]
    if s1 == s2:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
