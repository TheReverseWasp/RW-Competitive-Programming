movies = int(input())
saga = list(map(int,input().split()))
saga.sort()
saga = [str(elem) for elem in saga]
answer = saga[movies//3:movies//3+movies//3] +saga[:movies//3] +saga[movies//3+movies//3:]
print(" ".join(answer))
