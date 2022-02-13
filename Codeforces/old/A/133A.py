def main():
    c = input()
    for i in c:
        if i == "H" or i == "Q" or i == "9":
            print("YES")
            return
    print("NO")

if __name__ == "__main__":
    main()
