with open("test_case.txt", "w") as f:
    f.write("1000\n")
    for i in range(1,1001):
        f.write(str(i)+"\n")