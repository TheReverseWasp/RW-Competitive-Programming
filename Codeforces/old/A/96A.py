def main():
    ft = input()
    for i in range(len(ft) - 6):
        c = ft[i:i+7]
        flag = True
        for i in range(1,7):
            if c[i] != c[i - 1]:
                flag = False
                break
        if flag == True:
            print("YES")
            return True
    print("NO")

if __name__ == "__main__":
    main()