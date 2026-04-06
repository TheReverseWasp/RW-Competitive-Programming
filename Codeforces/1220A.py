n = int(input())
s = input()
ones, zeros = s.count("n"), s.count("z")
for i in range(ones):
    print(1,end=" ")
for i in range(zeros):
    print(0,end=" ")