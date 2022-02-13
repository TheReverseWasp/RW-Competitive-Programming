def analizer(n):
    flag = True
    for i in n:
        if i != "4" and i != "7":
            flag = False
            break
    return flag

def main():    
    n = input()
    flag = analizer(n)
    if flag == True:
        print("YES")
        return 0
    for i in range(1, int(n)):
        if int(n) % i == 0 and analizer(str(i)):
            print("YES")
            return 0
    print("NO")

if __name__ == "__main__":
    main()